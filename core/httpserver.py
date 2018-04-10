class SlowHTTPServer():
    '''SSLand built-in but slow WSGI server

    `server` is the WSGIServer instance.
    '''

    def __init__(self, wsgi_app, port=8000):
        from django.conf.urls import url
        from web.urls import urlpatterns
        def static_view(request, path):
            from django.http import HttpResponse, HttpResponseNotFound
            from django.contrib.staticfiles.finders import find
            import mimetypes
            fp = find(path)
            if fp:
                resp = HttpResponse(
                    file(fp, 'rb').read(),
                    content_type = mimetypes.guess_type(path, strict=False)[0]
                )
                resp['Cache-Control'] = 'max-age=300'
            else:
                resp = HttpResponseNotFound()
            return resp
        urlpatterns.append(url(r'^static/(?P<path>[^\?]+)$', static_view))
        from gevent.wsgi import WSGIServer
        http_server = WSGIServer(('', port), wsgi_app)
        http_server.serve_forever()

