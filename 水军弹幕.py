'''
目标：B站
弹幕地址格式，network里找msg。
'''
import time
import requests
import random


class DanMu():

    def __init__(self, room_id):
        self.url = 'https://api.live.bilibili.com/ajax/msg'
        self.room_id = room_id
        # 提交的参数
        self.form = {
            'roomid': self.room_id,
            'csrf_token': '123cd3e5b92cd4e233c3d984dda8cff2',
            'visit_id': '7jgh409b8600'
        }
        self.cookie = {'Cookie': 'finger=6759d89f; fts=1526569374; sid=kmel4h4z; DedeUserID=326767674; DedeUserID__ckMd5=be6eceba40a4c2d2; SESSDATA=fcd27c04%2C1529161392%2Cdd832725; bili_jct=123cd3e5b92cd4e233c3d984dda8cff2; bp_t_offset_326767674=69717635727375313; buvid3=58131411-FB95-4A36-84C8-9F38631DD3E7101608infoc; rpdid=oqxkxixkoxdosixsxlkqw; LIVE_BUVID=df79054ef31a8c96617fa1b4fd507b4d; LIVE_BUVID__ckMd5=8625cefadb84c4bf; LIVE_PLAYER_TYPE=2; UM_distinctid=163871130030-0083d82988351-3b7b0d58-100200-16387113004226; _dfcaptcha=a79282343456c8f067e75d06ef74633d; _jct=951dc9405dd311e8824d0242ac123ec9; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1526952300,1526958043,1526981360,1527002466; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1527002651'}

    def get(self):
        self.html = requests.post(self.url, data=self.form)
        danmu = list(map(lambda x: self.html.json()[
            'data']['room'][x]['text'], range(10)))
        self.message = danmu[random.randint(4, 9)]

    def send(self):
        self.send_url = 'https://api.live.bilibili.com/msg/send'
        self.send_form = {
            'color': 16777215,
            'csrf_token': '123cd3e5b92cd4e233c3d984dda8cff2',
            'fontsize': 25,
            'mode': 1,
            'msg': self.message,
            'rnd': 1527002649,
            'roomid': self.room_id
        }
        self.html = requests.post(
            self.send_url, data=self.send_form, cookies=self.cookie)
        print(self.html)


if __name__ == '__main__':
    # 实例化
    while True:
        B = DanMu(617484)
        B.get()
        B.send()
        # time.sleep(2)
