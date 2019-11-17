import json
# response = {"success": False, "message": "something went wrong", "data": []}

class HttpHandler:
    def code(self): return self.code


class HttpClientError(HttpHandler):

    def handle(self, code):
        if code == 404:
            response = {"success": False, "message": "something went wrong", "data": []}
            # return ' Page not found '
            return response

        if code == 500:
            return 'server error'


class Client:

    def __init__(self):
        self._handlers = []

    def add(self, error):
        self._handlers.append(error)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print(msg)
                # print(' Answer: % s ' % msg)
                break
        else:
            print(' Code not processed ')


z = Client()
z.add(HttpClientError())
z.response(404)
