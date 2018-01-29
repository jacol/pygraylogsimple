# pygraylogsimple
Simple graylog lib that use offsets and limits

##Usage
'''python

#initialize class with username, password and host
api = pygraylogsimple.PyGraylogSimple('user', 'password', 'http://host:port')

#use fuctions to access particular Graylog API method - last 2 params: offset and limit are optional
data = api.search_universal_absolute('*', '2017-07-01T00:00:00.000Z', '2017-07-02T00:00:00.000Z', 0, 100)

'''