## 1. 2019年华为测试题
> [**完整代码及相关NOTE**](https://github.com/pick-up-a-drop-of-water/Python_Notes/blob/master/Tests_Passed/huawei_test_handle_strings.py)
>
> **题目描述如下**
```python
"""
题目描述：
--  对输入字符串检查是否存在非法字符，输出合法字符串（去重）和非法字符串（不去重）
--  对合法字符串循环左移10次，在进行排序输出。（举例：比如字符串"abc"，循环左移一次的结果为"bca"）
输入描述：
(1) 字符串中的字符集合为 '0'-'9'，'a'-'z'，'A'-'Z'，其余为非法字符串（空字符串作为定界符），
    有非法字符的字符串被视为非法输入；
(2) 作为输入的字符串个数不超过100，每个字符串长度不超过64；
(3) 作为输入的连续空字符串（空格/制表符/回车/换行符）作为一个空格处理（作为定界符，字符串起始字符不能为空）；
(4) 输入每行只有一个字符串
(5) 输入以空行结束
输出描述：
(1) 输出合法字符串并去重
(2) 输出所有非法字符串
(3) 对结果1的去重合法字符串循环左移10次
(4) 对结果3合法字符串字符串排序，按ASCII表字符从小到大顺序排序
注意事项：
--  每输入一个字符后用空格跟下一个字符串隔离，作为输出的所有字符串之间只能有一个空格（作为定界符）；
示例1:
-- 输入
abc
def
==
acd123
44234tjg
aga'-=
ad--s
abd
123
abcdef
1234567890123456789012345678901234567890123
45678901234567890123
EDFG
SDFG
ABC
DEF
cccc
a*b=1
dd
87&&^
asdfas
234abc35
765rgfh4sd
1231
123
==
EDFG

-- 输出
abc def acd123 44234tjg abd 123 abcdef 1234
5678901234567890123456789012345678901234567
8901234567890123 EDFG SDFG ABC DEF cccc dd
asdfas 234abc35 765rgfh4sd 1231
== aga'-= as--s a*b=1 87&&^ ==
bca efd 23acd1 234tjg44 bda 231 efabcd 1234
5678901234567890123456789012345678901234567
8901231234567890 FGED FGSD BCA EFD cccc dd
asasdf 4abc3523 765rgfh4sd 3112
1234567890123456789012345678901234567890123
45678901231234567890 231 234tjg44 23acd1 31
12 4abc3523 765rgfh4sd BCA EFD FGED FGSD as
asdf bca bda cccc dd efabcd efd
"""
```
## 2. 2019年华为测试题
> [**完整代码**](https://github.com/pick-up-a-drop-of-water/Python_Notes/blob/master/Tests_Passed/rotate_matrix.py)
>
> **题目描述如下**
```python
"""
题目描述
输入一个N阶方阵(0<N<10),输出此方阵顺时针旋转M(0<=M<=10000)次后的方阵
旋转举例：（如下四个三阶方阵从上到下为数字围绕中心顺时针旋转）
1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3

9 8 7
6 5 4
3 2 1

3 6 9
2 5 8
1 4 7
输入描述：
输入第一行一个正整数N (0<N<10)
接下来N行每行N个整数用空格分开，为方阵的数据
接下来一行一个正整数M (0<=M<=10000)
说明：不用考虑异常输入，所有输入都是正常的，严格遵从取值范围
输出描述：
N行，每行N个整数，用空格分开，为旋转后的数据
示例1
输入
3
1 2 3
4 5 6
7 8 9
2
输出
9 8 7
6 5 4
3 2 1
"""
```
