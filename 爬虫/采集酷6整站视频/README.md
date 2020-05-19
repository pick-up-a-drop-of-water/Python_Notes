## [返回爬虫目录](https://github.com/pick-up-a-drop-of-water/Python_Notes#%E7%88%AC%E8%99%AB)
### 爬取酷6视频网站，并保存视频
> - 在XHR标签中，通过动态数据抓包获取的目标url
#### Code
> * 确定爬取的url路径，headers参数；
> * 发送请求 -- requests 模拟浏览器发送请求，获取响应数据；
> * 解析数据 -- json模块：把json字符串转化成python可交互的数据类型；
>     * 数据转换；
>     * 解析数据；
> * 保存数据。

```python
import requests
import json
import os

"""
# 1、确定爬取的url路径，headers参数
# 2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
# 3、解析数据 -- json模块：把json字符串转化成python可交互的数据类型
# 3.1 数据转换
# 3.2 解析数据
# 4、保存数据
"""


def download_video(page: str):
    # 1、确定爬取的url路径，headers参数
    # base_url = "https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectID=76"   # 问号后面的都属于请求参数，从XHR抓包获得的url
    base_url = "https://www.ku6.com/video/feed"   # 问号后面的都属于请求参数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36',
    }
    # 1.1、 请求参数
    params = {
        'pageNo': page,
        'pageSize': '40',
        'subjectID': '76'
    }
    # 2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
    response = requests.get(base_url, headers=headers, params=params)
    data = response.text
    # 3、解析数据 -- json模块：把json字符串转化成python可交互的数据类型
    # 3.1 数据转换
    json_data = json.loads(data)    # --字典
    # print(json_data)
    # 3.2 解析数据
    data_list = json_data['data']   # --列表

    for item in data_list:
        video_title = item['title'] + ".mp4"
        video_url = item['playUrl']
        # print(video_title, video_url)
        # 再次发送请求，请求视频数据【图像，音频都属于二进制数据，利用content访问】
        print("正在下载：{}".format(video_title))
        video_data = requests.get(video_url, headers=headers).content
        # 4、保存数据【wb写入二进制数据】
        if not os.path.exists('.\\video'):
            os.mkdir('video')
        with open('.\\video\\' + video_title, 'wb') as f:
            f.write(video_data)
            print("{} 下载完成...\n".format(video_title))


if __name__ == "__main__":
    for page in range(3):
        print("正在下载第{}页的数据".format(page + 1))
        download_video(page=str(page))



```
