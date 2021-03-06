# _*_ coding: utf-8 _*_
# @Project_Name : testactions
# @Time         : 2021/4/3 8:06
# @Author       : Gong-hub
# @Email        : 2821813806@qq.com
# @File         : test.py
# @Software     : PyCharm


from logging import getLogger
import requests, json ,urllib ,time
from bs4 import BeautifulSoup

logger = getLogger(__name__)
logger.info("starting")
def scrapy():
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }

    response = requests.get("https://www.bilibili.com/v/popular/rank/all",headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"html5lib")
        top100_list = soup.select("ul.rank-list > li")
        print(top100_list)
        data_list = []
        for item in top100_list:
            title = item.select("div.info > a.title")[0].get_text().replace(" ","").replace("\n","")
            author = item.select("span.data-box.up-name")[0].get_text().replace(" ","").replace("\n","")
            data_list.append([author,title])
        # return response.text
        return data_list
    else:
        return response.status_code

def sendTg(tgBot, content):
    try:
        token = tgBot['tgToken']
        chat_id = tgBot['tgUserId']
        #发送内容
        # content = str(content)
        text = ""
        for item in content:
            text += item[0]+"   "+item[1]+"\n"

        # data = {
        #     '***{} B站top100***'.format(time.strftime("%Y-%m-%d %H:%M:%S")):str(content)
        # }
        # content = urllib.parse.urlencode(data)
        #TG_BOT的token
        # token = os.environ.get('TG_TOKEN')
        #用户的ID
        # chat_id = os.environ.get('TG_USERID')
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}'
        session = requests.Session()
        resp = session.post(url,data={"text":text})
        print(resp)
    except Exception as e:
        print('Tg通知推送异常，原因为: ' + str(e))


def readJson():
    try:
        #用户配置信息
        with open('./config.json','r',encoding="UTF-8") as fp:
            users = json.load(fp)
            return users
    except Exception as e:
        logger.error('账号信息获取失败错误，原因为: ' + str(e))
        logger.error('1.请检查是否在Secrets添加了账号信息，以及添加的位置是否正确。')
        logger.error('2.填写之前，是否在网站验证过Json格式的正确性。')

def main():
    TGbot = readJson()["telegramBot"]
    sendTg(TGbot, scrapy())

if __name__ == '__main__':
    main()
    # print(scrapy())
