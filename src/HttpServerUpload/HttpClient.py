# !/usr/bin/env python
# coding=utf-8



from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

# 在 urllib2 上注册 http 流处理句柄
register_openers()

# 开始对文件 "DSC0001.jpg" 的 multiart/form-data 编码
# "image1" 是参数的名字，一般通过 HTML 中的  标签的 name 参数设置

# headers 包含必须的 Content-Type 和 Content-Length
# datagen 是一个生成器对象，返回编码过后的参数
datagen, headers = multipart_encode({"pyfile": open("PyHttpServerUpload.py", "rb")})

# 创建请求对象
request = urllib2.Request("http://115.231.37.33/fxupload.php", datagen, headers)
# 实际执行请求并取得返回
print urllib2.urlopen(request).read()