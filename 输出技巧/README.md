##### 【动态显示】
> - "\r"的使用
> - "end"的使用
> - "format"的使用
```python
for i in range(1000):
  for j in range(1000):
    print("\r{}\t{}\t{}\t{}".format(i, j, (i+j)%10**4, j-i), end="\t")
```
