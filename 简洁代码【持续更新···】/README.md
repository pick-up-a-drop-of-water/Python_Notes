##### 1. 字典
> - 字典与反向字典
```python
In [6]: x = {"This": 0, "is": 1, "original": 2, "code": 3}
In [7]: reverse_x = dict(zip(x.values(), x.keys()))
In [8]: reverse_x
Out[8]: {0: 'This', 1: 'is', 2: 'original', 3: 'code'}
In [9]: x
Out[9]: {'This': 0, 'is': 1, 'original': 2, 'code': 3} 
```
