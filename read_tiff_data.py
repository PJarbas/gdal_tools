# -*- coding: utf-8 -*-

import gdal
import matplotlib.pyplot as plt

"""
Read vhi tiff data and transform to array
"""

# read tiff data downloaded from nooa site
tif = gdal.Open('VHP.G04.C07.NP.P2017023.VH.VHI.tif')

f = tif.ReadAsArray()

plt.imshow(f)

plt.show()

