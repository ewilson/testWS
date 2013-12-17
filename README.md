testWS
======

A Flask web app for echoing requests. Sometimes useful for testing.

###Output###

    {
       "args":{
	        "baz":"true",
	        "foo":"bar"
       },
       "form":{

       },
       "headers":{
	        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	        "Accept-Encoding":"gzip,deflate,sdch",
      	        "Accept-Language":"en-US,en;q=0.8",
	        "Connection":"keep-alive",
	        "Content-Length":"",
	        "Content-Type":"",
	        "Cookie":"session=eyJjc3JmX3Rva2VuIjp7IiBiIjoiWTJWbU5qTmpaamc0TTJZMFl6bGtNelUwT1dJMFlXRTRPRFV6WVdFd09ESTNZMlpqTUROaE53PT0ifX0.BZIikg.ZoasTYWdaZ7dLAqy5tfyzfOkeG8",
	        "Host":"localhost:5000",
	        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
       },
       "method":"GET",
       "query_string":"foo=bar&baz=true",
       "url":"http://localhost:5000/?foo=bar&baz=true"
    }
