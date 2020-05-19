# vision-utils
Collection of random functions I have created over time that have proved useful for practical vision applications

# Docs
Since the sphinx docs are currently broke I will give some basic pointers here.

The primary object this library currently targets is the DataCollection object. This has a couple of handy methods. 
```python
from scalary import DataCollection

# Note: This will capture on your primary monitor by default.
dc = DataCollection() 

# Resize to something for acceptable for feeding into a CNN
dc.Record(region=(400, 40, 1500, 1000), resize=(480, 270))
```
