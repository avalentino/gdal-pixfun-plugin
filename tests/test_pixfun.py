#!/usr/bin/env python
###############################################################################
# $Id: pixfun.py 12181 2010-01-30 20:42:03Z valentino $
#
# Project:  GDAL/OGR Test Suite
# Purpose:  Test pixel functions support.
# Author:   Antonio Valentino <antonio.valentino@tiscali.it>
#
###############################################################################
# Copyright (c) 2010-2014, Antonio Valentino <antonio.valentino@tiscali.it>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################

import os
import unittest

import numpy as np
from osgeo import gdal

DATAPATH = os.path.dirname(__file__)


os.environ['GDAL_DRIVER_PATH'] = os.path.join(os.path.dirname(__file__),
                                              os.pardir)
gdal.AllRegister()


class TestPixfun(unittest.TestCase):

    def test_pixfun_real_c(self):
        filename = 'data/pixfun_real_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == refdata.real))

    def test_pixfun_real_r(self):
        filename = 'data/pixfun_real_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/int32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == refdata.real))

    def test_pixfun_imag_c(self):
        filename = 'data/pixfun_imag_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == refdata.imag))

    def test_pixfun_imag_r(self):
        filename = 'data/pixfun_imag_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == 0))

    def test_pixfun_mod_c(self):
        filename = 'data/pixfun_mod_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == np.abs(refdata)))

    def test_pixfun_mod_r(self):
        filename = 'data/pixfun_mod_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/int32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == np.abs(refdata)))

    def test_pixfun_phase_c(self):
        filename = 'data/pixfun_phase_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()
        refdata = refdata.astype('complex128')

        #self.assertTrue(np.allclose(data, np.arctan2(refdata.imag,
        #                                             refdata.real)))
        self.assertTrue(np.alltrue(data == np.arctan2(refdata.imag,
                                                      refdata.real)))

    def test_pixfun_phase_r(self):
        filename = 'data/pixfun_phase_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/pixfun_imag_c.vrt'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == np.arctan2(0, refdata)))

    def test_pixfun_conj_c(self):
        filename = 'data/pixfun_conj_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == np.conj(refdata)))

    def test_pixfun_conj_r(self):
        filename = 'data/pixfun_conj_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/int32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == np.conj(refdata)))

    def test_pixfun_sum_r(self):
        filename = 'data/pixfun_sum_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        refdata = np.zeros(data.shape, 'float')
        for reffilename in ('data/uint16.tif', 'data/int32.tif',
                            'data/float32.tif'):
            reffilename = os.path.join(DATAPATH, reffilename)
            refds = gdal.Open(reffilename)
            refdata += refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == refdata))

    def test_pixfun_sum_c(self):
        filename = 'data/pixfun_sum_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        refdata = np.zeros(data.shape, 'complex')
        for reffilename in ('data/uint16.tif', 'data/cint_sar.tif',
                            'data/cfloat64.tif'):
            reffilename = os.path.join(DATAPATH, reffilename)
            refds = gdal.Open(reffilename)
            refdata += refds.GetRasterBand(1).ReadAsArray(0, 0, 5, 6)

        self.assertTrue(np.alltrue(data == refdata))

    def test_pixfun_diff_r(self):
        filename = 'data/pixfun_diff_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/int32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata1 = refds.GetRasterBand(1).ReadAsArray(0, 0, 5, 6)

        reffilename = 'data/float32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata2 = refds.GetRasterBand(1).ReadAsArray(10, 10, 5, 6)

        self.assertTrue(np.alltrue(data == refdata1-refdata2))

    def test_pixfun_diff_c(self):
        filename = 'data/pixfun_diff_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata1 = refds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cfloat64.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata2 = refds.GetRasterBand(1).ReadAsArray(0, 0, 5, 6)

        self.assertTrue(np.alltrue(data == refdata1-refdata2))

    def test_pixfun_mul_r(self):
        filename = 'data/pixfun_mul_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        refdata = np.ones(data.shape, 'float')
        for reffilename in ('data/uint16.tif', 'data/int32.tif',
                            'data/float32.tif'):
            reffilename = os.path.join(DATAPATH, reffilename)
            refds = gdal.Open(reffilename)
            refdata *= refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == refdata))

    def test_pixfun_mul_c(self):
        filename = 'data/pixfun_mul_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == refdata*refdata))

    def test_pixfun_cmul_c(self):
        filename = 'data/pixfun_cmul_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == refdata*refdata.conj()))

    def test_pixfun_cmul_r(self):
        filename = 'data/pixfun_cmul_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/uint16.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata1 = refds.GetRasterBand(1).ReadAsArray()
        refdata1 = refdata1.astype('float64')

        reffilename = 'data/int32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata2 = refds.GetRasterBand(1).ReadAsArray()
        refdata2 = refdata2.astype('float64')

        self.assertTrue(np.alltrue(data == refdata1 * refdata2.conj()))

    def test_pixfun_inv_r(self):
        filename = 'data/pixfun_inv_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/uint16.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()
        refdata = refdata.astype('float64')

        self.assertTrue(np.alltrue(data == 1./refdata))

    def test_pixfun_inv_c(self):
        filename = 'data/pixfun_inv_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()
        refdata = refdata.astype('complex')

        self.assertTrue(np.allclose(data, 1./refdata))

    def test_pixfun_intensity_c(self):
        filename = 'data/pixfun_intensity_c.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/cint_sar.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == (refdata*refdata.conj()).real))

    def test_pixfun_intensity_r(self):
        filename = 'data/pixfun_intensity_r.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/float32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == (refdata*refdata.conj()).real))

    def test_pixfun_sqrt(self):
        filename = 'data/pixfun_sqrt.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/float32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == np.sqrt(refdata)))

    def test_pixfun_log10(self):
        filename = 'data/pixfun_log10.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/float32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.alltrue(data == np.log10(refdata)))

    def test_pixfun_dB2amp(self):
        filename = 'data/pixfun_dB2amp.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/float32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()

        self.assertTrue(np.allclose(data, 10.**(refdata/20.)))

    def test_pixfun_dB2pow(self):
        filename = 'data/pixfun_dB2pow.vrt'
        filename = os.path.join(DATAPATH, filename)
        ds = gdal.OpenShared(filename, gdal.GA_ReadOnly)
        data = ds.GetRasterBand(1).ReadAsArray()

        reffilename = 'data/float32.tif'
        reffilename = os.path.join(DATAPATH, reffilename)
        refds = gdal.Open(reffilename)
        refdata = refds.GetRasterBand(1).ReadAsArray()
        refdata = refdata.astype('float64')

        self.assertTrue(np.allclose(data, 10.**(refdata/10.)))


if __name__ == '__main__':
    unittest.main()
