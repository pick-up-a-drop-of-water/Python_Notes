### 使用Session：保持Cookie
> - Session是另一种记录客户状态的机制，不同的是 Cookie保存在客户端浏览器中，而 Session保存在服务器上。
> - 客户端浏览器访问服务器的时候，服务器把客户端信息以某种形式记录在服务器上。客户端浏览器再次访问时只需要从该 session中查找该客户的状态就可以了，这就是 Session。
> - 如果说 Cookie机制是通过检查客户身上的“通行证”来确定答户身份的话，那么 Session机制就是通过检查服务器上的客户明细表来确认客户身份。
> - Session相当于程序在服务器上建立的一份客户档案，客户来访的时候只需要查询客户档案表就可以了。
#### Code
> * 图片所对应url的base64编码问题
> * 回调：携带内容给后面的请求使用
```python
import requests

# 网站测试登录时，使用fake用户名及密码
# 有些图片链接需要添加base64解码，如下所示，删除64即可。
# https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand
# 此程序的验证码校验环节仍然需要人工识别位置，可参考相关机器识别分类算法，来提取相应验证位置坐标。

# 获取验证码
img_code_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
sess = requests.session()
res = sess.get(url=img_code_url).content
with open('code.png', 'wb') as f:
    f.write(res)

point_map = {
    "1": "40,45",
    "2": "116,53",
    "3": "185,52",
    "4": "257,50",
    "5": "49,121",
    "6": "116,133",
    "7": "185,132",
    "8": "257,139",
}
code_index = input("请输入验证码所对应位置1-8,多个用逗号分隔:")


def get_code_cord(index: str):
    code_cord = []
    ix_ls = index.split(',')
    for ix in ix_ls:
        code_cord.append(point_map[ix])
    return ",".join(code_cord)


# 校验验证码
check_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
params = {
    "answer": get_code_cord(code_index),
    "rand": "sjrand",
    "login_site": "E",
}
res = sess.get(url=check_url, params=params)
print(res.text)

```
