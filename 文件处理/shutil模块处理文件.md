# shulti模块处理
## 文件、文件夹的移动、复制、删除、重命名
> [参考链接](https://www.cnblogs.com/FengZiQ/p/8532141.html) :link:
- ### 相对路径
```python
import os
import shutil

deepwalk_path = "datasets/deepwalk/"
output_links_name = deepwalk_path + "deepwalk_needed_links.txt"
# copy and rename file to node2vec directory
node2vec_path = "datasets/node2vec/"
node2vec_file = node2vec_path + "node2vec_needed_links.txt"
shutil.copy(output_links_name, node2vec_file)
```
- ### 绝对路径
```python
#复制单个文件
shutil.copy("C:\\a\\1.txt","C:\\b")
#复制并重命名新文件
shutil.copy("C:\\a\\2.txt","C:\\b\\121.txt")
#复制整个目录(备份)
shutil.copytree("C:\\a","C:\\b\\new_a")

#删除文件
os.unlink("C:\\b\\1.txt")
os.unlink("C:\\b\\121.txt")
#删除空文件夹
try:
    os.rmdir("C:\\b\\new_a")
except Exception as ex:
    print("错误信息："+str(ex))#提示：错误信息，目录不是空的
#删除文件夹及内容
shutil.rmtree("C:\\b\\new_a")

#移动文件
shutil.move("C:\\a\\1.txt","C:\\b")
#移动文件夹
shutil.move("C:\\a\\c","C:\\b")

#重命名文件
shutil.move("C:\\a\\2.txt","C:\\a\\new2.txt")
#重命名文件夹
shutil.move("C:\\a\\d","C:\\a\\new_d")
```


