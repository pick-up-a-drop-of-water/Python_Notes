##### 1. 字典
> - 字典与反向字典
```python
x = {"This": 0, "is": 1, "original": 2, "code": 3}
reverse_x = dict(zip(x.values(), x.keys()))
"""
x
{'This': 0, 'is': 1, 'original': 2, 'code': 3} 
reverse_x
{0: 'This', 1: 'is', 2: 'original', 3: 'code'}
"""
```
