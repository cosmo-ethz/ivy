# Copyright (C) 2014 ETH Zurich, Institute for Astronomy


# Copyright (c) 2013 ETH Zurich, Institute of Astronomy, Lukas Gamper <lukas.gamper@usystems.ch>
'''
Created on Oct 7, 2013
@author: Lukas Gamper

'''
from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np

from ivy.plugin.base_plugin import BasePlugin


class Plugin(BasePlugin):
    """
    Show statistics of time.
    """
    def __call__(self):
        total = sum((timing.duration for timing in self.ctx.timings))
        print("== Ivy run took: {0:>7.3f} s ===".format(total))
        for timing in self.ctx.timings:
                print(timing)

    def __str__(self):
        return "stat"
