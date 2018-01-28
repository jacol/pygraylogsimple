import pycurl
import StringIO


class PyGraylogSimple:

    def __init__(self, user, password, host):
        self.user = user
        self.password = password
        self.host = host

    def getdata(self, querystring):
        response = StringIO.StringIO()
        c = pycurl.Curl()

        c.setopt(c.URL, self.host + querystring)
        c.setopt(c.WRITEFUNCTION, response.write)
        c.setopt(c.HTTPHEADER, ['Content-Type: application/json', 'Accept-Charset: UTF-8'])
        c.setopt(c.USERPWD, self.user + ':' + self.password)
        c.perform()
        c.close()

        result = response.getvalue()
        response.close()

        return result
