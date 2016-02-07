import tornado

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        print self
        self.render('index.html',UN= "Hello!")
