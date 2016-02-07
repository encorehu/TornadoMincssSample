import tornado

class DocsHandler(tornado.web.RequestHandler):
     def get(self):
        self.render('docs.html')
