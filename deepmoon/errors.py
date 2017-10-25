import dataset
import importlib
import random


class Errors(object):
    def __init__(self, filename=None, flavor=None):
        self.filename = filename or ':memory:'
        self.db = dataset.connect('sqlite:///{}'.format(self.filename))
        self.flavor = flavor or 'artisanal'
        source = importlib.import_module('deepmoon.{}'.format(self.flavor))
        self.errors = source.fetch_messages()
        self.seen = self.db[self.flavor]
        self.seen.create_column_by_example('comment', 'Snarky remark')
        self.seen.create_column_by_example('used', 1)
        self.seen.create_index('comment')
        random.shuffle(self.errors)
        self.at = 0

    def get(self):
        while self.seen.count(comment=self.errors[self.at],
                              used=1) > 0:
            self.at += 1
            if self.at == len(self.errors):
                self.at = 0
                self.seen.update({'used': 0}, [])
        result = self.errors[self.at]
        self.seen.upsert({'comment': self.errors[self.at], 'used': 1},
                         ['comment'])
        return result
    
