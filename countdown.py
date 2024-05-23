import keyboard
import time
import threading
import pygame

count = -1
count_lock = threading.Lock()  # 新增一個鎖來保護 count 變數

pygame.init()
pygame.mixer.init()

def countdown():
    global count
    while True:
        with count_lock:  # 使用 with 來確保在操作 count 變數時鎖住
            if count >= 0:
                print(count)
                mp3_file = f'mp3/{count}.mp3'
                play_music(mp3_file)
                
                count -= 1
        time.sleep(1)

def wait_for_key():
    global count
    while True:
        keyboard.wait('z')
        print('>> 重新倒數 <<')
        with count_lock:  # 使用 with 來確保在操作 count 變數時鎖住
            count = 15

def stop():
    global count
    while True:
        keyboard.wait('esc')
        print('>> 歸零 <<')
        with count_lock:  # 使用 with 來確保在操作 count 變數時鎖住
            count = -1

def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()


key_thread = threading.Thread(target=wait_for_key, daemon=True)
key_thread.start()

countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()

stop_thread = threading.Thread(target=stop)
stop_thread.start()

key_thread.join()
countdown_thread.join()
stop_thread.join()
