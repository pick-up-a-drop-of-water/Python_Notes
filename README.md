##### Links shared :airplane:
> - [Python 教程阅读简记](https://chyroc.cn/posts/python-tutorial-notes/)
> - [Python 语法之装饰器decorator](https://www.cnblogs.com/yutongzhu/p/5615764.html)
##### Python_Notes :book:
> - Record some magic commands or review codes!
##### Install tensorflow with conda in windows :smile:
```shell
conda create -n mlbook python=3.5 anaconda
conda activate mlbook
conda install --channel https://conda.anaconda.org/conda-forge tensorflow
# optionally install Jupyter extensions
conda install -n mlbook -c conda-forge jupyter_contrib_nbextensions
```
##### Ipython :dart:
###### magic commands :smirk:
1. %run xxx.py 运行python文件
2. 若.py不在当前目录下，在ipython终端可以使用系统命令，比如cd、ls等等；cd 时，可以直接把文件拖到终端窗口，自动生成文件路径（Linux）
3. %paste 复制粘贴板里的内容至终端（代码）
4. %timeit function(para1, para2, ...) 查看某函数的运行时间 
5. %pdb on 相当于在命令行中调试，若程序出错，可以打印变量的值。比如 p a(打印变量a的值)，p b(打印变量b的值)，最后q命令退出。不想用自动开调试，在ipython终端运行此命令：%pdb off
6. _(一个下划线)表示操作（命令）的上一个历史，__(两个下划线)表示上两个操作的历史
7. _34得到第34行输入代码的运行结果
8. _i34得到第34行输入代码
9. [Ipython快捷键](./pictures_stored/Ipython快捷键.png)
10. [常用的魔术命令](./pictures_stored/Ipython常用的魔术命令.png)

###### codes for numpy in Ipython :smile:

```python
'''
检验numpy的高效性
'''
def test(a, b):
	sum = 0
	for i,j in zip(a,b):
		sum += i*j
	return sum

import random
import numpy as np

# 产生随机数
# 产生10个1-20的随机整数
num = [random.randint(1,10) for i in range(20)]
# 产生10个10.0-20.0的随机小数且保留两位有效数字
prize = [round(random.uniform(10.0,20.0),2) for i in range(20)]

%timeit test(prize, num)
# output ：1.49 µs ± 33.7 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

prize_np = np.array(prize)
num_np = np.array(num)
%timeit np.dot(prize_np, num_np)
# output ：762 ns ± 1.07 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

np.arange(1,10,0.5) 			#步长可以设置为小数，range()不可以
np.linspace(0,10,15)			# 0到10分成15份

np.zeros(10, dtype='int')		#全零数组
np.zeros((3,5))				#二维全零数组(传元组)
np.zeros((3,5,10))			#三维全零数组
np.ones(10)				#全一数组

np.empty(10)				#不会有赋值操作(因此比np.zeros()快)，但产生的数值与之前内存存储值相关，亦可能是随机的

a = np.arange(15)
a = a.reshape(3,5)			#变为二维数组
# 等价于
a = np.arange(15).reshape(3,5)

np.ceil(3.5)	# 4 向上取整
np.floor(3.5)	# 3 向下取整
np.rint(3.5)	# 4 四舍五入
np.round(3.5)	# 4 四舍五入
np.around([0.12394, 1.255823],2)	# 保留2位小数, [0.12, 1.26]	

a = np.array([6,0])
b = np.array([2,0])
c = a/b
np.isnan(c)				# 有NaN值的位置对应为True
# output：array([False,  True])
# 利用其筛选元素
c[~np.isnan(c)]

# random模块自带的随机数生成函数
random.random()				# 返回0-1区间的随机数
random.randint(1,10)			# 返回指定区间1-10的随机数
random.uniform(1.0,10.0)		# 返回1.0-10.0区间的随机数
a = [1,2,3,4,5]
random.shuffle(a)			# 打乱给定列表的顺序
random.choice(a)			# 从给定列表中随机选一个值

# numpy模块中的随机数生成函数与之前类似
np.random.randint(1,10)			# 返回一个指定区间1-10的随机数
np.random.randint(1,10,5)		# 返回五个指定区间1-10的随机数
np.random.randint(1,10,(3,5))		# 返回3x5的数组，指定区间1-10的随机数
```
###### codes for pandas :smile:

```python
import pandas as pd
import numpy as np
a = pd.Series(np.arange(20))
'''
修改b,会改变原来a中对应的值
b = a[10:] 
b[10] = 222
此时a[10]变为222
同样的性质适用于numpy中array的操作
因此，赋值需谨慎！
'''
# 取a中第十个以后的元素，使用copy后，修改b，不会改变原来a中对应的值
b = a[10:].copy()
b
'''
Out[10]: 
10    10
11    11
12    12
13    13
14    14
15    15
16    16
17    17
18    18
19    19
dtype: int64
'''
# b[-1],b[0],b[5],b[9]都会出错，因为标签和下标（索引）冲突
# b[10]不会出错，因为既可以解释为标签也可以解释为下标（索引）
'''
如果索引是整数类型，则根据整数进行数据操作时总是面向标签的
所谓标签，即定义Series或Dataframe时指定的index，默认从0开始计数
eg：pd.Series(np.arange(5),index=list('abcde'))
loc			以标签解释
iloc		以下标解释
'''
# 取出b中的第一个元素
b.loc[10]	#以标签解释
b.iloc[0]	#以下标解释
# Dataframe索引和切片，和Series类似
df = pd.DataFrame({'one':list('1234'),
                   'two':list('4321')})
'''
Out[65]: 
  one two
0   1   4
1   2   3
2   3   2
3   4   1
'''
# 两种方式取第二列的第一行和第三行的元素
df.loc[[0,2],'two']		#列以标签解释
df.iloc[[0,2],1]		#列以下标解释
```
###### advancing codes for pandas :dart:

```python
import pandas as pd

'''
# 时间对象处理
pd.date_range('2019-01-01', '2019-03-18')
# freq = H(our),W(eek),B(usiness)
pd.date_range('2019-01-01', '2019-03-18', freq='W')
# 每周一
pd.date_range('2019-01-01', '2019-03-18', freq='W-MON')
# 产生100个周
pd.date_range('2019-03-18', periods=100, freq='W')
'''

# parse_dates：处理为时间对象
# 'date'（时间对象）作为索引
df = pd.read_csv('xxx.csv', index_col='date', parse_dates=['date'])

# 第一步：计算MA

## 方案1：手动计算
df['ma5'] = np.nan		# 5日均值
df['ma10'] = np.nan		# 10日均值

for i in range (4, len(df)):
	df.loc[df.index[i],'ma5'] = df.['close'][i-4:i+1].mean()

for i in range (9, len(df)):
	df.loc[df.index[i],'ma10'] = df.['close'][i-9:i+1].mean()
	
## 方案2：cumsum
sr = df['close'].cumsum()
df['ma5'] = (sr - sr.shift(1).fillna(0).shift(4)/5
df['ma10'] = (sr - sr.shift(1).fillna(0).shift(9)/10

## 方案3：rolling
df['ma5'] = df['close'].rolling(5).mean()
df['ma10'] = df['close'].rolling(10).mean()

# 第二步：找出金叉和死叉节点

df = df.dropna()

## 方案1：直接搜索
golden_cross = []				# ma5 由下往上穿 ma10 
death_cross = []				# ma5 又上往下穿 ma10

sr = df['ma10']>=df['ma5']			# 返回Bool变量的dataframe

for i in range(1, len(sr)):
	if sr.iloc[i] == True and sr.iloc[i-1] == False:
		death_cross.append(sr.index[i])
	if sr.iloc[i] == False and sr.iloc[i-1] == True:
		golden_cross.append(sr.index[i])
		
## 方案2：shift
death_cross = df[(df['ma10']>=df['ma5'])&(df['ma10']<df.['ma5']).shift(1)].index
golden_cross = df[(df['ma10']<=df['ma5'])&(df['ma10']>df.['ma5']).shift(1)].index

'''
# 其他操作
df.groupby('col_name')	
df.groupby('col_name').get_group('foo')	#get rows named 'foo' in group 'colname'
pd.merge(df1, df2)
pd.merge(df1, df2, on='col_name')
'''
```
###### 其他重要操作 :+1:
01. ###### 合并数据帧
```python
# miRNA_disease_data = pd.concat([miRNA_disease_pos_df, miRNA_disease_neg_df])
# or
miRNA_disease_data = miRNA_disease_pos_df.append(miRNA_disease_neg_df)
miRNA_disease_data = miRNA_disease_data.reset_index(drop=True)
```
02. ###### 根据相关列的值从DataFrame中选择行
> [参考链接](https://vimsky.com/article/3842.html)
```python
link2removed = ['D-65::mi-143', 'D-65::mi-144', 'D-65::mi-145', 'D-65::mi-156', 'D-65::mi-160', 'D-65::mi-180']
ix_filtered = disease_miRNA_pos_df['links'].isin(link2removed)
disease_miRNA_specify_pos_df = disease_miRNA_pos_df[ix_filtered].reset_index(drop=True)
disease_miRNA_filtered_pos_df = disease_miRNA_pos_df[~ix_filtered].reset_index(drop=True)
```
