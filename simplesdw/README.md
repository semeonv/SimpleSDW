# simplesdw
SimpleSDW is simple and fast way to use the European Central Bank's Statistical Warehouse Data with Python.

![logo](https://i.ibb.co/Ks41qJ2/SIMPLE-1.png)
# Simple-SDW
SimpleSDW is simple and fast way to use the European Central Bank's [Statistical Warehouse Database]('https://sdw.ecb.europa.eu/') with python.

**How to install:**
```
pip install -i https://test.pypi.org/simple/ ssdw==0.0.1
```
### Requirements
There is only one library required to have installed before using **simplesdw**
* Pandas
* _Matploitlib is recommended to visualize the data_

How to install **pandas**:
```
pip install pandas
```
How to install matploitlib
```
python -m pip install -U matplotlib
```

### Introduction
A simple look on how to easily incorporate the **simplesdw** library in you project:
1) Start by importing the library
2) Create the SDW object
3) Fill in the four variables depending on the timeseries you want to use from https://sdw.ecb.europa.eu/
   * At this point you can use any **pandas** function to manipulate the dataframe
4) Plot the timeseries using **matplotlib**

### Sample Code
This should be enough to help you understand how the **simplesdw** library works:
```python
from simplesdw import sdw as ecb
import matplotlib.pyplot as plt

startDate = '2004-01-01'
endDate = '2022-08-01'

# The Statistical Database Warehouse gives id's in this format: LFSI.M.I8.S.UNEHRT.TOTAL0.15_74.T
# As a user you need to grab the first few letters which is the flowRef
# The rest is the "key" which further specifies the type of data
# For example the "M" stands for monthly data
flowRef = 'LFSI'
key = 'M.I8.S.UNEHRT.TOTAL0.15_74.T'

unemployment_r = ecb.SDW(flowRef, key, startDate, endDate)
ts_u = unemployment_r.setup()

plt.plot(ts_u)
plt.show()

```