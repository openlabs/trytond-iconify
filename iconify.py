# -*- coding: utf-8 -*-
"""
    iconify.py

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import os

from trytond.tools import file_open
from trytond.pool import PoolMeta

__metaclass__ = PoolMeta
__all__ = ['Icon']


class Icon:
    __name__ = 'ir.ui.icon'

    # Dictionary of icons which need to be replaced.
    # eg. 'tryton-list': 'icons/name-of-icon.svg'
    better_icons = {}

    def get_icon(self, name):
        """
        If we have a fresh icon for the purpose, return that instead of
        the sad icons tryton comes with. What a pity!
        """
        if self.name in self.better_icons:
            path = self.better_icons[self.name]
            path = os.path.join('iconify', path.replace('/', os.sep))
            with file_open(path, subdir='modules') as fp:
                return fp.read()
        return super(Icon, self).get_icon(name)
