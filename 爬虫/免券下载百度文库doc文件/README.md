### 免券下载百度文库中数据格式为doc的文件
> - 与之前的免券下载百度文库txt文件类似
>> - 关键是找到提取doc文件的url，再分析提取json数据
#### Code
> - 参考于该[链接](https://www.52pojie.cn/thread-1012567-1-3.html)
```python
import requests
import re
import json
import os
from tqdm import tqdm


class Baidu_doc(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        self.rtcs_flag = '1'
        self.rtcs_ver = '3.1'
        self.base_url = 'http://wkrtcs.bdimg.com/rtcs/webapp'
        self.flag = True
        self.cout = 1

        self.bucketNum = None
        self.sign = None
        self.rsign = None
        self.md5sum = None
        self.page_list = None
        self.page_count = None
        self.firstpageurl = None
        self.name = None
        self.save_path = None

    def get_info(self, url):
        try:
            content = requests.get(url, headers=self.headers).content.decode()
        except Exception:
            print('编码异常,切换为GBK编码!')
            content = requests.get(url, headers=self.headers).content.decode('gbk')
        # 查看网页源代码
        # print(content)
        self.bucketNum = re.findall('"bucketNum":(\\d+),', content)[0]
        self.sign = re.findall('&sign=(.*?)&', content)[0]
        self.rsign = re.findall('"rsign":"(.*?)",', content)[0]
        self.md5sum = re.findall('&md5sum=(.*?)&', content)[0]
        self.page_list = re.findall('"rtcs_range_info":(.*),"rtcs_flow"', content)[0]
        self.page_count = re.findall('"rtcs_page_count":(.*?),', content)[0]
        self.firstpageurl = re.findall('data-firstpageurl="(.*?)"', content)[0].replace('amp;', '')
        try:
            self.name = re.findall('<title>(.*?)</title>', content)[0].strip()
        except Exception:
            self.name = '未命名-百度文库'
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        self.save_path = self.name + '/'

    # 解析一页文档
    def get_page(self, page: int):
        """
        第一页url：
        https://wkrtcs.bdimg.com/rtcs/webapp?bucketNum=90&pn=1&rn=1&md5sum=b56d133048e0fa62c0701a65bd84d926&sign=7c0961017d&rtcs_flag=1&rtcs_ver=3&range=0-13969&rsign=p_9-r_0-s_2c311&callback=sf_edu_wenku_rtcs_doc_jsonp_1_1
        文档所有页的url为:
        https://wkrtcs.bdimg.com/rtcs/webapp?bucketNum=90&pn=1&rn=9&md5sum=b56d133048e0fa62c0701a65bd84d926&sign=7c0961017d&rtcs_flag=1&rtcs_ver=3&range=0-13969&rsign=p_9-r_0-s_2c311&callback=sf_edu_wenku_rtcs_doc_jsonp_1_1
        """
        # 文档第一页url，以第一页为基准进行修改
        pattern = re.compile("pn=\d+")
        doc_url = re.sub(pattern, "pn={}".format(str(page)), self.firstpageurl)
        # 文档url
        page_dic_ls = json.loads(self.page_list)
        page_dic = page_dic_ls[page - 1]
        doc_url = re.sub("range=\\d+-\\d+", "range={}".format(page_dic.get("range")), doc_url)
        print("第{}页url: \n".format(str(page)), doc_url)
        response = requests.get(url=doc_url, headers=self.headers).text
        document = response[32:-1]
        document_dict = json.loads(document)
        output = ''
        # 访问doc文档结构内容并保存
        for item_dict in tqdm(document_dict['document.xml']):
            for item in item_dict['c']:
                output += '\n'
                for content in item['c']:
                    try:
                        if isinstance(content['c'], str):
                            output += content['c']
                    except Exception:
                        pass
        with open(self.save_path + self.name + '.doc', 'a', encoding='utf-8') as f:
            f.write(output)

    # 解析所有页文档
    def get_doc(self):
        print("原网页：", url)
        for page in range(1, int(self.page_count) + 1):
            self.get_page(page)
        print('{}的所有页面解析完成，已保存为doc文档。'.format(self.name))

    def run(self, url):
        self.get_info(url)
        self.get_doc()


if __name__ == '__main__':
    # url = input('请输入网址:')
    url = "https://wenku.baidu.com/view/f7440c8d7e192279168884868762caaedd33bae5.html?from=search"
    doc = Baidu_doc()
    doc.run(url)

```

