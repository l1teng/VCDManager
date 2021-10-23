import argparse
from abc import ABC, abstractmethod


class BaseOptions(ABC):
    def __init__(self):
        self.initialized = False

    @abstractmethod
    def initialize(self, parser):
        parser.add_argument('--db', type=str, default='VCD_MANAGER', help='# is the remote db')
        parser.add_argument('--db_ip', type=str, default='127.0.0.1', help='# is the ip address of remote db')
        parser.add_argument('--db_port', type=int, default=3306, help='# is the port of remote db')
        parser.add_argument('--db_user', type=str, default='root', help='# is the admin user of remote db')
        parser.add_argument('--db_passwd', type=str, default='5315', help='# is the password of remote db')
        self.initialized = True

    def gather_ops(self):
        if not self.initialized:
            parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
            parser = self.initialize(parser)
        # opt, _ = parser.parse_known_args()
        self.parser = parser

        return parser.parse_args()

    @property
    def status(self):
        return 'Parser initialized: {}.'.format(self.initialized)

    def parse(self):
        opt = self.gather_ops()
        self.opt = opt

        return self.opt
