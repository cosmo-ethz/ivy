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


'''
Created on Mar 5, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals
from ivy.plugin.base_plugin import BasePlugin


class Plugin(BasePlugin):
    '''
    Plugin that computes the square of ctx.value
    '''
    
    def __str__(self):
        return __name__
    
    def __call__(self):
        self.ctx.value = self.ctx.value**2
#         s = 0 
#         for i in range(10**3):
#             for j in range(10**3):
#                 s += i*j
