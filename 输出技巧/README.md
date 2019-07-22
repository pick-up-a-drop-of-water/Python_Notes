#### 【动态显示】
> - "\r"的使用
> - "end"的使用
> - "format"的使用
```python
for i in range(1000):
  for j in range(1000):
    print("\r{}\t{}\t{}\t{}".format(i, j, (i+j)%10**4, j-i), end="\t")
```
#### 【不使用format】
> - "{}"结合"f"的使用技巧
> - 输出结果与【动态显示】的运行结果一致
```python
for i in range(1000):
  for j in range(1000):
      print(f"\r{i}\t{j}\t{(i+j%10**4)}\t{j-i}", end="\t")
```
#### 【显示进度条】
> - [Tqdm模块的使用](https://blog.csdn.net/qq_33472765/article/details/82940843)
#### 【显示运行时间】
> - datetime模块的使用
```python
from datetime import datetime

start_time = datetime.now()
print("开始时间: ", start_time.strftime("%Y-%m-%d %H:%M:%S"))


def display_runtime():
    end_time = datetime.now()
    print("结束时间: ", end_time.strftime("%Y-%m-%d %H:%M:%S"))
    run_time = end_time - start_time
    print("运行时间: ", run_time.seconds, "秒")
```
