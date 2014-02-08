wtd
===

What the Diff

Get started
-----------

install https://github.com/jkbr/httpie
or use chrome + postman extensions for REST

```
mkvirtualenv wtd
workon wtd
pip install -r requirements.txt
./manage.py syncdb
./manage.py runserver_plus --threaded
```

then you can

```
$ http POST localhost:8000/wtd/ uri=http://localhost:8000/test_diff/

HTTP/1.0 200 OK
Allow: POST, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 08 Feb 2014 23:24:45 GMT
Server: Werkzeug/0.9.4 Python/2.7.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "diff": null,
    "meta": {
        "has_diff": false,
        "num_diff": 0
    }
}
```

Make a change to 

```
wtd/apps/core/tempaltes/test/test_diff.html
```

and hit it again

```
$ http POST localhost:8000/wtd/ uri=http://localhost:8000/test_diff/

HTTP/1.0 200 OK
Allow: POST, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 08 Feb 2014 23:25:32 GMT
Server: Werkzeug/0.9.4 Python/2.7.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "diff": "--- \n+++ \n@@ -2,3 +2,5 @@\n \n test Body\n \n+test Body too\n+",
    "meta": {
        "has_diff": true,
        "num_diff": 8
    }
}
```