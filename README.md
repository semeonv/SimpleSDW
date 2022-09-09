# simple-sdw
Simple-SDW is simple and fast way to use the European Central Bank's Statistical Warehouse Database with python.
![logo](https://i.ibb.co/Ks41qJ2/SIMPLE-1.png)
# Simple-SDW
Simple-SDW is simple and fast way to use the European Central Bank's [Statistical Warehouse Database]('https://sdw.ecb.europa.eu/') with python.

How to install:
```python
pip install simplesdw
```

### Introduction
A simple look on how to easily incorporate the **simplesdw** library in you project:
1) Start by importing the library
2) Create the SDW object
3) Fill in the four variables depending on the timeseries you want to use from https://sdw.ecb.europa.eu/
   * At this point you can use any **pandas** function to manipulate the dataframe
4) Plot the timeseries using **matplotlib**
```python
from simplesdw import sdw
import matplotlib.pyplot as plt

ecb = SDW.setup()

startDate = '2004-01-01'
endDate = '2022-08-01'

flowRef = 'LFSI'
key = 'M.I8.S.UNEHRT.TOTAL0.15_74.T'

unemployment_r = ecb.SDW(flowRef, key, startDate, endDate)
ts_u = unemployment_r.setup()

plt.plot(ts_u)
plt.show()

```
