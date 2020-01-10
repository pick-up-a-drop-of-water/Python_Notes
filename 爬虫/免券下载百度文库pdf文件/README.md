### 免券下载百度文库pdf文件
> - 目前只支持下载pdf是图片的文档
### Code
```python
import requests
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
}

session = requests.session()        # 帮助保存cookie信息，保持登录状态等


# 发送请求，获取内容
def fetch_url(url):
    response = session.get(url, headers=headers)
    # response.encoding = response.apparent_encoding
    # print(session.get(url).content.decode('gbk'))       # html源代码是gbk
    return response.content.decode('gbk')


def parser_title(content):
    try:
        return re.findall(r'"docTitle":"(.*?)"', content)[0]
    except:
        return re.findall(r"title.*?:.*?\'(.*?)\',", content)[0]


def parser_type(content):
    try:
        return re.findall(r'"docType":"(.*?)"', content)[0]
    except:
        return re.findall(r"docType: '(.*?)'", content)[0]


def get_doc_id(content):
    # https://wenku.baidu.com/view/cbb4af8b783e0912a3162a89.html?from=search
    try:
        return re.findall(r'"doc_id":"(.*?)"', content)[0]
    except:
        return re.findall(r'name="doc_id".*?value="(.*?)"', content)[0]


def get_doc_page_num(content):
    try:
        return re.findall(r'"totalPageNum":"(.*?)"', content)[0]
    except:
        return re.findall(r"'totalPageNum':.*?'(\d+)'", content)[0]


# 获取pdf某一页的回调信息，并返回当前页pdf所对应url
def get_callback_infos(doc_id, page):
    """
    'https://wenku.baidu.com/browse/getrequest?doc_id=4d6f5d1ee3bd960590c69ec3d5bbfd0a7956d5e7&pn=1&rn=1&type=ppt&callback=bd__cbs__72kxdq'
    # pn表示返回第几页开始的信息，rn表示返回从pn页开始共rn页的信息 ==>
    # 存储为字典列表[{}]，可从中提取md5sum、sign、png等相关信息
    # {"zoom":"https:\/\/wkretype.bdimg.com\/retype\/zoom\/ed0fb02a3968011ca3009152?pn=1&raww=1080&rawh=810&o=jpg_6&md5sum=511e84218f27039b919a32250d8424eb&sign=f1507489c2&png=0-49642&jpg=0-75988","page":1}
    'https://wenku.baidu.com/browse/getrequest?doc_id=4d6f5d1ee3bd960590c69ec3d5bbfd0a7956d5e7&pn=1&rn=1&type=ppt'
    """
    infos_url = 'https://wenku.baidu.com/browse/getrequest?doc_id={}&pn={}&rn=1&type=ppt'.format(doc_id, page)
    infos = fetch_url(infos_url)
    # zoom后缀
    zoom_suffix = re.findall(r'zoom\\/(.*?)\?', infos)[0]
    # md5值
    md5 = re.findall('&md5sum=(.*?)&', infos)[0]
    # print(md5)
    # sign
    sign = re.findall('&sign=(.*?)&', infos)[0]
    # png
    png = re.findall('&png=(.*?)&', infos)[0]
    # jpg
    jpg = re.findall(r'&jpg=(.*?)\"', infos)[0]

    """
    分析pdf图片对应url

    https://wkretype.bdimg.com/retype/zoom/ed0fb02a3968011ca3009152?pn=1&o=jpg_6&
    md5sum=511e84218f27039b919a32250d8424eb&sign=f1507489c2&png=0-49642&jpg=0-75988

    https://wkretype.bdimg.com/retype/zoom/ed0fb02a3968011ca3009152?pn=2&o=jpg_6&
    md5sum=511e84218f27039b919a32250d8424eb&sign=f1507489c2&png=49643-95401&jpg=75989-206336

    https://wkretype.bdimg.com/retype/zoom/ed0fb02a3968011ca3009152?pn=3&o=jpg_6
    &md5sum=511e84218f27039b919a32250d8424eb&sign=f1507489c2&png=95402-100796&jpg=206337-302464

    """
    pdf_url = 'https://wkretype.bdimg.com/retype/zoom/{}?pn={}&o=jpg_6' \
              '&md5sum={}&sign={}&png={}&jpg={}'.format(zoom_suffix, page, md5, sign, png, jpg)
    return pdf_url


def download_pdf(pdf_url):
    pdf_content = requests.get(pdf_url, headers=headers).content
    # print(pdf_content)
    return pdf_content


def save_pdf(file_name, pdf, page: int):
    save_path = './pdf/' + file_name + '/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    with open(save_path + str(page) + ".jpg", "wb") as f:
        f.write(pdf)
    print("第{}页pdf图片已保存！".format(page + 1))


def init_data(content):
    title = parser_title(content)
    doc_type = parser_type(content)
    doc_id = get_doc_id(content)
    doc_page_num = get_doc_page_num(content)
    print((title, doc_type, doc_id, doc_page_num))
    return title, doc_type, doc_id, doc_page_num


if __name__ == '__main__':
    # url = 'https://wenku.baidu.com/view/4d6f5d1ee3bd960590c69ec3d5bbfd0a7956d5e7.html?from=search'    # 测试用
    url = 'https://wenku.baidu.com/view/4937ef0fa100a6c30c22590102020740be1ecd22.html?from=search'
    content = fetch_url(url)
    print(content)
    title, doc_type, doc_id, doc_page_num = init_data(content)
    for page in range(1, int(doc_page_num) + 1):
        # 获取pdf url
        pdf_url = get_callback_infos(doc_id, page=page)
        pdf = download_pdf(pdf_url)
        save_pdf(file_name=title, pdf=pdf, page=page)



```
