# gdal tips for data analysis


### GDAL

##### Convert netCDF file to TIFF.

```$ gdal_translate file.nc file.tif```

##### Convert TIFF file to netCDF.

```$ gdal_translate -of "NetCDF" file.tif file.nc```

##### Convert HDF file to netCDF.
```$ gdalinfo file.hdf```

select one of the subdatasets
the name is all after SUBDATASET_n_NAME=
then
```$ gdal_translate -of "NetCDF" subdataset_name file.nc```

reference: http://www.gdal.org/frmt_hdf4.html

