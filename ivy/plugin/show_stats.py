# IVY is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# IVY is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with IVY.  If not, see <http://www.gnu.org/licenses/>.



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
