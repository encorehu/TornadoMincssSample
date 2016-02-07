import tornado

class DownloadHandler(tornado.web.RequestHandler):
     def get(self):
        self.render('download.html')
