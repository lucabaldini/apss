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

def pdf(phi, m, phi0=0):
    """Probability density function.
    """
    return 1. / (2 * np.pi) * (1 + m * np.cos(2 * (phi - phi0)))

def cf(phi, m, phi0=0):
    """Cumulative function for a modulation curve.
    """
    return 0.5 + 1. / (2 * np.pi) * (phi + 0.5 * m * np.sin(2 * (phi - phi0)))


m = np.linspace(0., 1., 200)
phi = np.linspace(-np.pi, np.pi, 200)
z = pdf(*np.meshgrid(phi, m)).T

plt.figure()
plt.contourf(m, phi, z, 75, cmap=plt.get_cmap('afmhot'))
plt.colorbar().set_label('pdf')
plt.xlabel('m')
plt.ylabel('$\\phi$ [rad]')

