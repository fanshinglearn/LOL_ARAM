import time
import tkinter as tk
import threading
import requests
import json

from lol_controller import LOL

with open('aram.json', 'r', encoding='utf8') as jfile:
    aram_jdata = json.load(jfile)

stop_flag = threading.Event()

def afk():
    while not stop_flag.is_set():
        is_in_game, game_type, team = opgg_is_in_game()

        wait_for_crawler()

        if is_in_game:
            msg = f'遊戲模式: {game_type}\n隊伍: {team}'
            L1.config(text=msg)
            if team == '藍隊':
                enemy_caastle_pos = aram_jdata['pos']['red_castle']
            else:
                enemy_caastle_pos = aram_jdata['pos']['blue_castle']
            LOL.click(enemy_caastle_pos)
            LOL.attack(enemy_caastle_pos)
        else:
            msg = '沒有在進行對戰 .w.'
            L1.config(text=msg)

        countdown(30)

def opgg_is_in_game():
    player_id = '1nXTkNy9PF9RGpU4P_kFz-49_aze2BUmOXCtJDPOuPsw3_IZY9cRPA2Hlg'
    # player_id = '2KtkxfOatsf6pxMDNQoYeAjonaFOQd39UoO3q9Lt_jOQ9XdjpaklJ1Gj4w'
    # player_id = 'cBiVrEiglrR7UxYmyyN6piDyMO95zZKaInQkOdJIiLB1G2zManubh9gyyw'
    url = f'https://lol-web-api.op.gg/api/v1.0/internal/bypass/spectates/tw/{player_id}?hl=zh_TW'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    r = requests.get(url, headers=headers)
    is_in_game = True if r.status_code == 200 else False
    game_type = r.json()['data']['queue_info']['queue_translate'] if is_in_game else None
    if is_in_game:
        for summoner in r.json()['data']['participants']:
            if summoner['summoner']['summoner_id'] == player_id:
                team_key = summoner['team_key']
                break
        team = '藍隊' if team_key == 'BLUE' else '紅隊'
    else:
        team = None
    return is_in_game, game_type, team

def wait_for_crawler():
    msg = '查詢中'
    for _ in range(3):
        msg += '.'
        L1.config(text=msg)
        time.sleep(0.5)

def countdown(seconds):
    for i in range(seconds, -1, -1):
        if stop_flag.is_set():
            L2.config(text='')
            break
        L2.config(text=i)
        time.sleep(1)

def start_afk():
    global stop_flag
    stop_flag.clear()  # 每次點擊開始都清除 stop_flag
    thread = threading.Thread(target=afk)
    thread.daemon = True  # 確保程式退出時執行緒自動退出
    thread.start()
    start_btn.config(state=tk.DISABLED)

def stop_afk():
    stop_flag.set()
    start_btn.config(state=tk.NORMAL)
    L1.config(text='暫停 .w.')

root = tk.Tk()
root.geometry("200x200+800+300")
root.resizable(0, 0)
root.title('ARAM 掛機')

# 設置視窗置頂
root.attributes("-topmost", True)

# root.wm_attributes("-transparentcolor", "aqua")
# root.configure(bg='aqua')


# < ------------------------------ 上半 ------------------------------ >
F1=tk.LabelFrame(root)
F1.pack(padx=10, pady=10)

# 開始按鈕
start_btn = tk.Button(F1, text='開始', command=start_afk)
start_btn.pack(side='left', padx=10, pady=10)

# 暫停按鈕
stop_btn = tk.Button(F1, text='暫停', command=stop_afk)
stop_btn.pack(side='left', padx=10, pady=10)

# < ------------------------------ 下半 ------------------------------ >
F2=tk.LabelFrame(root)
F2.pack(padx=10, pady=10)

# 顯示狀態的Label
L1 = tk.Label(F2, text='L1')
L1.pack(padx=10, pady=10)

L2 = tk.Label(F2, text='L2')
L2.pack(padx=10, pady=10)

root.mainloop()
