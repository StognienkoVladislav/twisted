
from datetime import datetime
from twisted.web.util import redirectTo


def render_get(self, request):
    return redirectTo(datetime.now().year, request)

