##### 【动态显示】
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
