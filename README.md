# gdal tips for data analysis


### GDAL

##### Convert netCDF file to TIFF.

```$ gdal_translate file.nc file.tif```

##### Convert TIFF file to netCDF.

```$ gdal_translate -of "NetCDF" file.tif file.nc```


