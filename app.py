import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from urls import urlpatterns

define("port", default=8888, help="run on the given port", type=int)

class TornadoApplication(tornado.web.Application):

    def __init__(self):
        handlers = urlpatterns
        settings = dict(
            debug=True,
            cookie_secret="bGlmZSBpcyBzaG9ydCwgaSBsaWtlIHB5dGhvbg==",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path= os.path.join(os.path.dirname(__file__), "static")

        )
        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(TornadoApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
