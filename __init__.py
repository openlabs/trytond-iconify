# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from iconify import Icon


def register():
    Pool.register(
        Icon,
        module='iconify', type_='model'
    )
