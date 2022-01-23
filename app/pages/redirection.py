from flask import redirect


class Redirection:

    def __init__(self, url):
        self.url = url

    def render(self):
        return redirect(self.url)
