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
import numpy as np
from matplotlib import pyplot as plt

plt.ion()


def pdf(phi, m, phi0=0):
    """Probability density function.
    """
    return 1. / (2 * np.pi) * (1 + m * np.cos(2 * (phi - phi0)))

def cf(phi, m, phi0=0):
    """Cumulative function.
    """
    return 1. / (2 * np.pi) * (phi + 0.5 * m * np.sin(2 * (phi - phi0)))

def ppf(phi, m, phi0=0):
    """Percent-point function.

    Drop a line to luca.baldini@pi.infn.it if you do have a closed-form 
    complete solution to this that can be expressed in terms of elementary
    functions!
    """
    return None


phi = np.linspace(-np.pi, np.pi, 100)
plt.figure()
for m in [0., 0.25, 0.5, 0.75, 1.0]:
    y = pdf(phi, m)
    plt.plot(phi, y, label='m = %.2f' % m)
plt.legend()
plt.xlabel('$\\phi$ [rad]')
plt.ylabel('pdf')
plt.savefig('cos2_pdf.pdf')

phi = np.linspace(-np.pi, np.pi, 100)
plt.figure()
for m in [0., 0.25, 0.5, 0.75, 1.0]:
    y = cf(phi, m)
    plt.plot(phi, y, label='m = %.2f' % m)
plt.legend()
plt.xlabel('$\\phi$ [rad]')
plt.ylabel('cf')
plt.savefig('cos2_cf.pdf')
