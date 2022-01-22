from flask import render_template


class Message:

    def __init__(self, config, name, text):
        self.config = config
        self.name = name
        self.text = text

    def render(self):
        return render_template('message.html', app_name=self.config['APP_NAME'], page_title=self.name, message=self.text)
