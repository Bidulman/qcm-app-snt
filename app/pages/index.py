from .page import Page


class Index(Page):

    def __init__(self, config, api):
        super().__init__(config, api, False, None, 'Bienvenue', 'index.html')

    def script(self, **args):
        return {}
