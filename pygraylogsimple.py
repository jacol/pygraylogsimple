import pycurl
from io import BytesIO
import json

class PyGraylogSimple:

    def __init__(self, user, password, host, limit_per_request):
        self.user = user
        self.password = password
        self.host = host
        self.limit_per_request = limit_per_request

    def _build_search_universal_absolute_url(self, query, date_time_from, date_time_to):
        return '{0}/search/universal/absolute?query={1}&from={2}&to={3}&limit={4}'. \
            format(self.host, query, date_time_from, date_time_to, self.limit_per_request)

    def search_universal_absolute(self, query, date_time_from, date_time_to):
        url = self._build_search_universal_absolute_url(query, date_time_from, date_time_to)

        all_messages = []
        offset = 0

        graylog_response = _GraylogResponse([], 0)

        while offset <= graylog_response.total_messages:
            full_url = url + '&offset=' + str(offset)
            graylog_response = self._run(full_url)
            all_messages.extend(graylog_response.messages)
            offset += self.limit_per_request

        return all_messages

    def _run(self, url):
        response = BytesIO()
        curl = _CurlInvoker()
        curl.call(url, self.user, self.password, response)
        result = response.getvalue()
        response.close()

        json_data = json.loads(result)
        return _GraylogResponse(json_data['messages'], json_data['total_results'])


class _CurlInvoker:

    @staticmethod
    def call(url, user, password, response_to_fill):
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, response_to_fill.write)
        c.setopt(c.HTTPHEADER, ['Content-Type: application/json', 'Accept-Charset: UTF-8'])
        c.setopt(c.USERPWD, user + ':' + password)
        c.perform()
        c.close()


class _GraylogResponse:
    messages = []
    total_messages = 1

    def __init__(self, messages, total_messages):
        self.messages = messages
        self.total_messages = total_messages
