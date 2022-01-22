from flask import request

from .page import Page, Message


class Login(Page):

    def __init__(self, config, api, **static):
        super().__init__(config, api, False, None, 'Connexion', 'login.html', **static)

    def script(self, **args):
        return {}


class PostLogin(Page):

    def __init__(self, config, api):
        super().__init__(config, api, True, None, None, None)

    def script(self, **args):
        username = request.form.get('username')
        password = request.form.get('password')

        response = self.api.request('put', '/sessions', data={'session': {'username': username, 'password': password}})

        if response.status_code == 404:
            return Login(self.config, self.api, messages=[('error-message', "L'utilisateur est inconnu. Peut-être vous-êtes vous trompés en notant vos identifiants ?")])

        return Message(self.config, 'Connexion réussie !', 'Vous vous êtes connecté.')