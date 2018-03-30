
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

import time


class CLockPage(Resource):
    isLeaf = True

    def render_GET(self, request):
        return "The local time is {}".format(time.ctime())


resource = CLockPage()
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()
