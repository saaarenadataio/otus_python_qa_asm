Echo-server, returns header of request
Custom status must be sent as '?status=417' to be parsed
How to test:
1) Run python script (host and port set as the vars)
2) Try to request server with client, e.g.:
 - curl: curl 'http://localhost:8099?status=417' 
 - browser: http://localhost:8099
