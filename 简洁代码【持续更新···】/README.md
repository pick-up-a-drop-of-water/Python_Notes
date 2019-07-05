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
##### 2.随机数
> - np.random.choice()
```python
# 无放回随机
np.random.choice(10, 10, replace=False)
# array([4, 2, 3, 8, 7, 1, 6, 5, 0, 9])
# 有放回随机
np.random.choice(10, 10, replace=True)
# array([7, 1, 3, 9, 6, 3, 5, 9, 2, 9]) ==> 有重复数字3、9
```
