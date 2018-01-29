# pygraylogsimple
Simple graylog lib that use offsets and limits

## Usage

Initialize class with username, password, host and limit for each request to API

'api = pygraylogsimple.PyGraylogSimple('user', 'pass', 'http://<host>:<port>', 100)'

Call function with query and date_time from and to

'data = api.search_universal_absolute('*', '2017-07-01T00:00:00.000Z', '2017-07-02T00:00:00.000Z')'
