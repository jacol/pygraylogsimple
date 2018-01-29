import pycurl
import StringIO


class PyGraylogSimple:

    def __init__(self, user, password, host):
        self.user = user
        self.password = password
        self.host = host

    def build_search_universal_absolute_url(self, query, date_time_from, date_time_to):
        """
        :param query: use * for everything
        :param date_time_from: format - 2017-07-01T00:00:00.000Z
        :param date_time_to: format - 2017-07-01T00:00:00.000Z
        :return: complete url to Graylog API
        """
        return '{0}/search/universal/absolute?query={1}&from={2}&to={3}'. \
            format(self.host, query, date_time_from, date_time_to)

    def run_query(self, url, offset=None, limit=None):
        """
        :param url: complete url to call
        :param offset: optional
        :param limit: optional
        :return: response from Graylog API as string
        """

        response = StringIO.StringIO()
        c = pycurl.Curl()

        if offset is not None:
            url += '&offset=' + str(offset)

        if limit is not None:
            url += '&limit=' + str(limit)

        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, response.write)
        c.setopt(c.HTTPHEADER, ['Content-Type: application/json', 'Accept-Charset: UTF-8'])
        c.setopt(c.USERPWD, self.user + ':' + self.password)
        c.setopt(c.HEADERFUNCTION, response.write)
        c.perform()
        c.close()

        result = response.getvalue()
        response.close()

        return result
