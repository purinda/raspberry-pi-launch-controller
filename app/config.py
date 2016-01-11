import yaml


class Config(object):
    def __init__(self, fn):
        self.config = yaml.load(file(fn, 'r'))

    def get(self, key, default=None):
        path = key.split('.')
        conf = self.config

        for item in path:
            if item in conf:
                conf = conf[item]
            else:
                return default

        return conf
