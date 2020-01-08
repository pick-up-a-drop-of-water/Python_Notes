### 下载百度千千音乐
> - 步骤
>   - 提供歌手名
>   - 获取该歌手所有歌曲ID
>   - 获取对应歌曲的名称和下载链接
>   - 下载保存
#### Code
> - 关键点
>   - json格式的数据写入与读取
>   - 抓取Ajax动态加载的网页
>   - 利用content保存音频等二进制文件
```python

import requests
import re
import json
from pprint import pprint
import os


# 写入读取字典格式的数据 for json文件
class JsonFile(object):
    @staticmethod
    def save_file(path, content_dict):
        # 先将字典对象转化为可写入文本的字符串
        content_dict = json.dumps(content_dict, ensure_ascii=True, indent=4)
        try:
            with open(path, "w", encoding='utf-8') as f:
                f.write(content_dict)
        except Exception as e:
            print("写入json文件出错：", e)

    @staticmethod
    def load_file(path):
        with open(path, 'r') as f:
            b = f.read()
            b.encode("utf-8-sig")
            id_singer_dict = json.loads(b)
            # 利用pprint打印json格式数据
            # pprint(id_singer_dict)
            return id_singer_dict


# 获取歌曲ID所对应的名字及链接
def get_song_links(song_id):
    url = "http://play.taihe.com/data/music/songlink"
    params = {
        'songIds': song_id,
    }
    response = requests.post(url=url, params=params)
    # 提取json文件中的字典信息
    music_infos = response.json()['data']['songList']
    for music_info in music_infos:
        song_name = music_info['songName']
        song_link = music_info['songLink']
        yield song_name, song_link


# 获取该歌手的所有歌曲ID
def get_song_ids(singer_id):
    response = requests.get("http://music.taihe.com/artist/{}".format(singer_id))
    response.encoding = response.apparent_encoding      # 解决编码问题
    song_ids_ls = re.findall('href="/song/(\\d+)', response.text, re.S)
    print(song_ids_ls)
    return song_ids_ls


# 获取所有歌手的ID
def get_singer_ids():
    path = '.\\id_singer.json'
    if not os.path.exists(path):
        base_url = 'http://music.taihe.com/artist'
        response = requests.get(base_url)
        response.encoding = response.apparent_encoding
        id_singers = re.findall('<a href="/artist/(\\d+)" title="(.*?)"', response.text, re.S)
        id_singer_dict = {}
        for id_singer in id_singers:
            id = id_singer[0]
            singer = id_singer[1]
            if singer not in id_singer_dict:
                id_singer_dict[singer] = id
        # 将歌手id和歌手名字保存为json格式文件
        JsonFile.save_file(path=path, content_dict=id_singer_dict)
        id_singer_dict = JsonFile.load_file(path=path)
        return id_singer_dict
    else:
        print("歌手ID信息已存在，导入中......")
        id_singer_dict = JsonFile.load_file(path=path)
        return id_singer_dict


# 返回该歌手的所有歌曲ID
def init_data(singer_name):
    id_singer_dict = get_singer_ids()
    # 获取歌手ID
    singer_id = id_singer_dict[singer_name]
    # 获取该歌手的所有歌曲ID
    song_ids = get_song_ids(singer_id)
    song_ids = ",".join(song_ids)

    return song_ids


# 下载音乐
def download_music(name_links, singer_name):
    # 下载mp3的文件夹
    save_path = ".\\music\\{}\\".format(singer_name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 下载mp3
    for name_link in name_links:
        print(name_link)
        song_name = name_link[0]
        song_link = name_link[1]
        try:
            # 图片、音频是二进制数据，用content访问
            response = requests.get(song_link)
            with open(save_path + song_name + ".mp3", "wb") as f:
                f.write(response.content)
        except Exception as e:
            print("这首歌曲请求出错：", e)


# 网站暂未进行反爬
if __name__ == "__main__":
    singer_name = input('请输入歌手姓名:')
    # 返回该歌手的所有歌曲ID
    song_ids = init_data(singer_name)
    # 获取歌曲ID所对应的名字及链接
    name_links = get_song_links(song_ids)
    # 下载音乐
    download_music(name_links, singer_name)



```
