import time
import tkinter as tk
import threading
import requests

stop_flag = threading.Event()

def test():
    while not stop_flag.is_set():
        print("Running infinite loop...")
        time.sleep(1)

def start_afk():
    global stop_flag
    stop_flag.clear()  # 每次點擊開始都清除 stop_flag
    thread = threading.Thread(target=test)
    thread.daemon = True  # 確保程式退出時執行緒自動退出
    thread.start()
    start_btn.config(state=tk.DISABLED)

def stop_afk():
    stop_flag.set()
    start_btn.config(state=tk.NORMAL)
    L1.config(text='Thread Stopped')

root = tk.Tk()
root.geometry("200x200+800+300")
root.resizable(0, 0)
root.title('ARAM 掛機')

# 設置視窗置頂
root.attributes("-topmost", True)

# 開始按鈕
start_btn = tk.Button(root, text='開始', command=start_afk)
start_btn.pack(padx=10, pady=10)

# 結束按鈕
stop_btn = tk.Button(root, text='結束', command=stop_afk)
stop_btn.pack(padx=10, pady=10)

# 顯示狀態的Label
L1 = tk.Label(root, text='')
L1.pack(padx=10, pady=10)

root.mainloop()
