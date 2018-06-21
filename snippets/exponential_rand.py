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
from matplotlib import pyplot as plt

plt.ion()


def ppf(q, lambda_=1):
    """Percent-point function for the exponential distribution.
    """
    return -np.log(1. - q) / lambda_

q = np.random.uniform(size=10) 
v = ppf(q)

x = np.linspace(0, 1, 100)
# Mind you will get a runtime warning here, when x = 1.!
y = ppf(x, 1.)
plt.figure()
plt.plot(x, y)
for _q in np.linspace(0, 1, 20):
    _v = ppf(_q)
    plt.plot([_q, _q], [0, _v], color='gray', lw=0.75, ls='dotted')
    plt.plot([_q, 0], [_v, _v], color='gray', lw=0.75, ls='dotted')
plt.xlabel('q')
plt.ylabel('ppf(q)')
plt.savefig('exponential_rand.pdf')
