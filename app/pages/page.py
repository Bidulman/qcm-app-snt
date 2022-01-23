from flask import render_template, request, Response
from .message import Message
from .redirection import Redirection


class Page:

    def __init__(self, config, api, needs_api, needed_permission, name, template, **static):
        self.config = config
        self.api = api
        self.needs_api = needs_api
        self.needed_permission = needed_permission
        self.name = name
        self.template = template
        self.static = static

    def process(self, **args):
        if self.needs_api and not self.api.test():
            return Message(self.config, 'Erreur API', "Le service de données est actuellement indisponible.")
        if self.needed_permission:
            token = request.args.get('token')
            if not token:
                return Message(self.config, 'Authentification inexistante', "Vous n'êtes pas authentifié dans l'application.")
            response = self.api.request('get', '/sessions', data={'session': {'token': token}})
            print(response)
            print(response.json())
            if not self.config['USER_PERMISSIONS'][response.json()['permission']] <= self.config['USER_PERMISSIONS'][self.needed_permission]:
                return Message(self.config, 'Permission non accordée', "Vous n'êtes pas autorisé à procéder à cette action.")
        return self.script(**args)

    def script(self, **args):
        return {}

    def render(self, **args):
        process = self.process(**args)
        if isinstance(process, Page) or isinstance(process, Message) or isinstance(process, Redirection):
            return process.render()
        messages = []
        if request.args.get('messages'):
            messages = [message.split('|') for message in request.args.get('messages').split(',')]
        token = None
        if request.args.get('token'):
            token = request.args.get('token')
        return render_template(self.template, token=token, app_name=self.config['APP_NAME'], page_title=self.name, app_address=self.config['APP_ADDRESS'], **self.static, **process, messages=messages)
