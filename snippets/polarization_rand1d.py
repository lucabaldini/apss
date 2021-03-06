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
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

plt.ion()


def fit_function(phi, N, m, phi0):
    """Fit function (essentially the pdf with a normalization constant).
    """
    return N / (2 * np.pi) * (1 + m * np.cos(2 * (phi - phi0)))

def cf(phi, m=0.5, phi0=0):
    """Cumulative function for a modulation curve (note we set m=0.5 by default)
    """
    return 0.5 + 1. / (2 * np.pi) * (phi + 0.5 * m * np.sin(2 * (phi - phi0)))


x = np.linspace(-np.pi, np.pi, 100)
y = cf(x)

cf_spline = InterpolatedUnivariateSpline(x, y, k=3)
ppf_spline = InterpolatedUnivariateSpline(y, x, k=3)

plt.figure()
plt.plot(x, cf_spline(x))
plt.xlabel('$\phi$ [rad]')
plt.ylabel('$F(\phi)$')

plt.figure()
q = np.linspace(0., 1., 100)
plt.plot(q, ppf_spline(q))
plt.xlabel('$q$')
plt.ylabel('$ppf(q)$')
plt.savefig('cos2_ppf_spline1d.pdf')

plt.figure()
phi = ppf_spline(np.random.uniform(size=100000))
n, bins, patches = plt.hist(phi, bins=100)
bin_centers = 0.5 * (bins[:-1] + bins[1:])
plt.xlabel('$\phi$ [rad]')
plt.ylabel('Entries / bin')
popt, pcov = curve_fit(fit_function, bin_centers, n, (1, 1, 0.), np.sqrt(n))
plt.plot(x, fit_function(x, *popt))
m = popt[1]
dm = np.sqrt(pcov[1, 1])
phi0 = popt[2]
dphi0 = np.sqrt(pcov[2, 2])
plt.text(0.7, 1500, '$m = %.3f \\pm %.3f$' % (m, dm))
plt.text(0.7, 1400, '$\\phi_0 = %.3f \\pm %.3f$' % (phi0, dphi0))
plt.savefig('cos2_rand1d.pdf')
