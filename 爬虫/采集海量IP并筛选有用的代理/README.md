## [返回爬虫目录](https://github.com/pick-up-a-drop-of-water/Python_Notes#%E7%88%AC%E8%99%AB)
### 可爬取的免费代理IP网站
>- http://www.66ip.cn/1.html
>- http://www.ip3366.net/free/?stype=1&page=1
>- http://www.kuaidaili.com/free/inha/1/
>- http://www.xicidaili.com/nn/1
>- http://www.ip3366.net/?stype=1&page=1
>- http://www.iphai.com/
>- http://www.data5u.com/
    
#### 采集海量IP，并筛选出有用的代理
> - 高匿代理IP：隐藏本机的IP地址
> - 使用正则匹配，提取网页中的高匿代理IP
##### ing
- [ ] 可以尝试从多个代理网站上爬取IP，构造代理IP池
- [ ] 尝试多线程爬取
- [ ] 尝试利用数据库构造代理IP池，便于增删改查
##### 西刺代理
> - 正则匹配，提取代理IP
> - 爬取时，最好添加随机延时，增加不被封的可能性
```python
import requests
import re


def get_ips(url="https://www.xicidaili.com/nn/1"):
    # 目标网址
    url = url
    # 使用get方法请求数据
    response = requests.get(url, headers=headers)       # 添加headers反爬， 从浏览器上复制下来
    html = response.text
    """
    正则匹配如下格式内容：
    <td>223.242.247.12</td>
          <td>9999</td>
    """
    # re.S 忽略【空格】换行符的干扰，正则匹配ip和port，注意匹配内容间的括号，注意中间的换行符和空格的匹配
    ips_ports = re.findall("<td>(\\d+\\.\\d+\\.\\d+\\.\\d+)</td>\\n +?<td>(\\d+)</td>", html, re.S)
    for ip_port in ips_ports:
        ip = ip_port[0]
        port = ip_port[1]
        proxies = {
            "http": "http://" + ip + ":" + port,
            "https": "http://" + ip + ":" + port,
        }
        try:
            res = requests.get("http://www.baidu.com", proxies=proxies, timeout=3)
            print(proxies["http"])
            print(proxies["https"], "能使用\n")
            # 保存有效ip
            with open("ip.txt", mode="a+") as f:
                f.write(ip + ":" + port + "\n")
        except Exception as e:
            print(proxies["http"])
            print(proxies["https"], "不能使用\n")


if __name__ == "__main__":
    website = 'https://www.xicidaili.com/nn/'
    for page in range(1, 10):
        print("爬取第{}页代理IP".format(page))
        get_ips(url=website + str(page))



```
