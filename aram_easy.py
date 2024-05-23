import time
import json

from lol_controller import LOL

with open('aram.json', 'r', encoding='utf8') as jfile:
    aram_jdata = json.load(jfile)

# 等待切換畫面
time.sleep(3)

while True:
    # LOL.attack(aram_jdata['pos']['blue_castle'])
    LOL.attack(aram_jdata['pos']['red_castle'])
    time.sleep(30)
