from .page import Page


class Index(Page):

    def __init__(self, config, api, **static):
        super().__init__(config, api, False, None, 'Bienvenue', 'index.html', **static)

    def script(self, **args):
        return {}
