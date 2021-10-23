from abc import ABC

from .base_options import BaseOptions


class VCDManagerOpt(BaseOptions, ABC):
    def initialize(self, parser):
        super(VCDManagerOpt, self).initialize(parser)
        # parser.add_argument('--db', type=str, default='VCD_MANAGER', help='# is the remote db')

        return parser
