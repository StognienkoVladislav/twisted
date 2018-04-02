
from twisted.internet import reactor
from twisted.enterprise import adbapi


dbpool = adbapi.ConnectionPool("sqlite3", "users.db.db")


def getName(email):
    return dbpool.runQuery("SELECT name FROM users.db WHERE email = ?", (email,))


def printResults(results):
    for elt in results:
        print(elt[0])


def finish():
    dbpool.close()
    reactor.stop()


d = getName("ajne@foo.com")
d.addCallback(printResults)

reactor.callLater(1, finish)
reactor.run()
