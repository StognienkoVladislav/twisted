
import time

from twisted.internet import reactor, threads
from twisted.internet.task import LoopingCall


def blockingApiCall(arg):
    time.sleep(1)
    return arg


def nonblockingCall(arg):
    print(arg)


def printResult(result):
    print(result)


def finish():
    reactor.stop()


d = threads.deferToThread(blockingApiCall, "Go")
d.addCallback(printResult)

LoopingCall(nonblockingCall, "NoGo").start(.25)

reactor.callLater(2, finish)
reactor.run()

