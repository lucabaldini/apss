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


import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from matplotlib import pyplot as plt

plt.ion()

x = np.linspace(0., 1., 10)
y = np.exp(3. * x) * np.sin(3. * x)

s1 = InterpolatedUnivariateSpline(x, y, k=1)
s3 = InterpolatedUnivariateSpline(x, y, k=3)

grid = np.linspace(0., 1., 100)
plt.figure()
plt.plot(x, y, 'o')
plt.plot(grid, s1(grid), label='Linear interpolating spline')
plt.plot(grid, s3(grid), label='Cubic interpolating spline')
plt.legend()
plt.savefig('spline.pdf')
