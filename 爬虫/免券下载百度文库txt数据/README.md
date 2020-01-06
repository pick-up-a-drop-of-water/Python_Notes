### 下载百度文库中数据格式为txt的文件

> - 利用session保存cookie信息，以保持登录状态
>> - 首先根据文档网页源代码，查询提取文档id、文档类型、文档标题
>> - 在文档源代码中找到文件所在的内容url
>> - 分析内容url的网页源代码，利用正则提取md5、页码、rsign等信息，以组成一个新的内容url
>> - 提取新的内容url的网页源代码
>> - 解析json数据，保存为txt文件

#### Code
> - 参考于该[链接](https://www.iqiyi.com/v_19rwla6hr4.html "视频链接")
```python
import requests
import re
import json

session = requests.session()        # 帮助保存cookie信息，保持登录状态等


# 发送请求，获取内容
def fetch_url(url):
    print(session.get(url).content.decode('gbk'))       # html源代码是gbk
    return session.get(url).content.decode('gbk')


def get_doc_id(url):
    # https://wenku.baidu.com/view/cbb4af8b783e0912a3162a89.html?from=search
    return re.findall("view/(.*?).html", url)[0]


def parser_type(content):
    return re.findall(r"docType.*?:.*?\'(.*?)\',", content)[0]


def parser_title(content):
    return re.findall(r"title.*?:.*?\'(.*?)\',", content)[0]


# 提取文本内容
def parser_txt(doc_id):
    content_url = "https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=" + doc_id
    content = fetch_url(content_url)
    # md5值
    md5 = re.findall('"md5sum":"(.*?)"', content)[0]
    print(md5)
    # 页码
    pn = re.findall('"totalPageNum":"(.*?)"', content)[0]
    # rsign
    rsign = re.findall('"rsign":"(.*?)"', content)[0]

    content_urls = "https://wkretype.bdimg.com/retype/text/" + doc_id + "?rn=" + pn + "&type=txt" + md5 + "&rsign=" + rsign
    content = json.loads(fetch_url(content_urls))
    result = ''
    for item in content:
        for i in item['parags']:
            result += i['c'].replace('\\r', '\r').replace('\\n', '\n')
    return result


# 保存
def save_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print("已保存为：" + filename)


# 主函数
def main():
    url = "https://wenku.baidu.com/view/6b1184cc580216fc710afd82.html?from=search"
    # 请求
    content = fetch_url(url)
    # 获取id
    doc_id = get_doc_id(url)
    # print(doc_id)
    # 文档类型
    type = parser_type(content)
    print(type)
    # 标题
    title = parser_title(content)
    print(title)
    if type == 'txt':
        result = parser_txt(doc_id)
        save_file(title + '.txt', result)


if __name__ == '__main__':
    main()
```
