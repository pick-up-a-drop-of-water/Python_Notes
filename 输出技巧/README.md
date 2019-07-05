##### print
> - "\r"的使用
> - "end"的使用
> - "format"的使用
```python
for i in range(1000):
  for j in range(1000):
    print("\r{}\t{}\t{}\t{}".format(i, j, i+j, j-i), end="\t")
```
