from invenio_base.signals import app_loaded

from . import config

# from oarepo_actions.ext import test


class SampleExt(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.init_config(app)

    #      app_loaded.connect(test)

    def init_config(self, app):
        for k in dir(config):
            if k.startswith('RECORDS_'):
                value = getattr(config, k)
                if isinstance(value, dict):
                    app.config.setdefault(k, {}).update(value)
                else:
                    app.config[k] = value
        print('Sample config initialized')
