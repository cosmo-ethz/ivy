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
    Simple implementation of the BasePlugin
    '''
    
    def __init__(self, ctx, **kwargs):
        self.value = kwargs.pop("value", None)
        super(Plugin, self).__init__(ctx, **kwargs)
        
    def __str__(self):
        return __name__
    
    def __call__(self):
        if self.value is not None:
            print(self.value)
