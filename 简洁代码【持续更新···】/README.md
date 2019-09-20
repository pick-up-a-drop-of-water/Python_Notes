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
##### 3.排序
> - 给定一个二维数组，按照差值大小，升序排列
```python
"""
输入: [[13, 19], [4, 9], [10, 20]]
输出：[[10, 20], [13, 19], [4, 9]]
"""
nums = [[13, 19], [4, 9], [10, 20]]
nums.sort(key=lambda x: x[0] - x[1])   # 差值升序排序
```
> - 给定一个二维数组，按照每一行第二个元素，降序排列
```python
"""
输入: [[13, 19], [4, 9], [10, 20]]
输出: [[10, 20], [13, 19], [4, 9]] 
"""
# 输入数据生成二维数组: N * ?
N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
nums_sorted = sorted(nums, key=(lambda x: x[1]), reverse=True)
# 当不需要保存nums排序前的值时，可这样使用
# nums.sort(key=(lambda x: x[2]), reverse=True)
```
##### 4.zip、map妙用:
```python
"""
输入:
    1 3 2
    5 4 6
    8 9 7
输出：[3, 2] + [6, 5] + [9, 8]
    [18, 15]
"""
m = 2
ls_1 = list(map(int, input().split()))
ls_1.sort(reverse=True)
ls_2 = list(map(int, input().split()))
ls_2.sort(reverse=True)
ls_3 = list(map(int, input().split()))
ls_3.sort(reverse=True)

result = list(map(lambda x: x[0] + x[1] + x[2], zip(ls_1[:m], ls_2[:m], ls_3[:m])))

print(result)
```
##### 5.快速生成A~Z字符数组
str_ls = list(''.join(map(chr, range(65, 91))))
