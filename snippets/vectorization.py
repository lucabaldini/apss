#***********************************************************************
# Copyright (C) 2018 Luca Baldini (luca.baldini@pi.infn.it)
#
# For the license terms see the file LICENSE, distributed along with this
# software.
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#***********************************************************************
from __future__ import print_function, division


import random
import time
import numpy as np

# How many random numbers (uniformly distributed between 0 and 1) do you
# want to throw?
n = 1000000

# The slow way: explicit for loop in Python.
t0 = time.time()
x = []
for i in range(n):
    x.append(random.random())
dt = time.time() - t0
print('Elapsed time: %.3f s' % dt)

# The quick way: vectorizing in numpy
t0 = time.time()
x = np.random.random(size=n)
dt = time.time() - t0
print('Elapsed time: %.3f s' % dt)
