# -*-coding: utf-8 -*-

import json
from os.path import join


class ConfigDict(dict):
    def __getitem__(self, item):
        return self.__getattribute__(item)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)


class Config:
    def __init__(self, path=join('etc', 'config.json')):
        self.config = self._read(path)

    def _read(self, path):
        with open(path) as f:
            config = json.load(f)
        return config

    @classmethod
    def load(cls, dictobj):
        if not isinstance(dictobj, dict):
            return dictobj

        config = ConfigDict()
        for k, v in dictobj.items():
            config[k] = cls.load(v)
        return config

