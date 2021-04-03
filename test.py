# _*_ coding: utf-8 _*_
# @Project_Name : testactions
# @Time         : 2021/4/3 8:06
# @Author       : Gong-hub
# @Email        : 2821813806@qq.com
# @File         : test.py
# @Software     : PyCharm


from logging import getLogger
import requests

logger = getLogger(__name__)
logger.info("starting")

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

response = requests.get("https://www.bilibili.com/v/popular/rank/all")
if response.status_code == 200:
    print(response.text)


