
from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol


class QuoteProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numConnections += 1

    def dataReceived(self, data):
        print("Number of active connections: {}".format(self.factory.numConnections))
        print("> Received: ``{}''\n> Sending: ``{}''".format(data, self.getQuote()))
        self.transport.write(self.getQuote())
