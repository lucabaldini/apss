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


def norm(t):
    """
    """
    return 1 + 0.01 * t


def Gamma(t):
    """
    """
    return 2 - 0.01 * t


def energy_spectrum(E, t):
    """
    """
    return norm(t) * E**(-Gamma(t))
    

t = np.linspace(0., 100., 100)
E = np.linspace(1., 10., 100)

plt.figure()
z = energy_spectrum(*np.meshgrid(E, t)).T
plt.contourf(t, E, z, 75, cmap=plt.get_cmap('afmhot'))
plt.colorbar().set_label('$pdf(\\phi; m, \\phi_0 = 0)$')
plt.xlabel('t [s]')
plt.ylabel('E [kev]')
plt.savefig('spectrum.pdf')
