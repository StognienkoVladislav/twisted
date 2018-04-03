
from twisted.internet import protocol, reactor


class EchoProcessProtocol(protocol.ProcessProtocol):
    def connectionMade(self):
        print("connectionMade called")
        reactor.callLater(10, self.terminateProcess)

    def terminateProcess(self):
        self.transport.signalProcess("TERM")

    def outReceived(self, data):
        print("outReceived called with {} bytes of data: {}".format(len(data), data))

    def errReceived(self, data):
        print("errReceived called with {} bytes of data: {}".format(len(data), data))

    def inConnectionLost(self):
        print("inConnectionLost called, stdin closed.")

    def outConnectionLost(self):
        print("outConnectionLost called, stderr closed.")

    def processExited(self, reason):
        print("processExited called with status {}".format(reason.value.exitCode))
        reactor.stop()


pp = EchoProcessProtocol()

commandAndArgs = ["twistd", "-ny", "echo_server.tac"]
reactor.spawnProcess(pp, commandAndArgs[0], args=commandAndArgs)
reactor.run()
