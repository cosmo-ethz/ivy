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
from ivy.config import base_config
from ivy.loop import Loop

plugins = Loop(["test.plugin.simple_plugin",
                "test.plugin.simple_plugin"
                ])

a=None
b=None
c=None
d=None
e=None
f=None
g=None
h=None
i=None
j=None

bool1 = True
bool2 = True
bool3 = False
bool4 = False