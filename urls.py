from handlers.index import IndexHandler
from handlers.example import ExampleHandler
from handlers.docs import DocsHandler
from handlers.download import DownloadHandler
from handlers.bootstrapconverter import BootstrapConverterHandler


urlpatterns  = [
    (r'/', IndexHandler),
    (r'/index.html', IndexHandler),
    (r'/example.html', ExampleHandler),
    (r'/docs.html', DocsHandler),
    (r'/download.html', DownloadHandler),
    (r'/bootstrapconverter.html', BootstrapConverterHandler),

]