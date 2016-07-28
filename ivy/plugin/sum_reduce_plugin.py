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
Created on Mar 18, 2014

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals


class Plugin(object):
    '''
    classdocs
    '''


    def __init__(self, ctx):
        '''
        Constructor
        '''
        self.ctx = ctx
    
    def reduce(self, ctxList):
        sum = 0
        for ctx in ctxList:
            sum += ctx.value
        
        self.ctx.valuesSum = sum