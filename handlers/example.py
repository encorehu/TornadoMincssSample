import tornado

class ExampleHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('example.html',UN= "Hello!")
