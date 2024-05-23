import asyncio
import edge_tts
import pygame
import time

# voice = 'zh-CN-YunxiNeural'
voice = 'zh-CN-XiaoyiNeural'

async def amain() -> None:
    for i in range(15, -1, -1):
        text = f'{i}'
        output_file = f'mp3/{i}.mp3'
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)

asyncio.run(amain())

# def play_music(music_file):
#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(music_file)
#     pygame.mixer.music.play()

# play_music('test.mp3')
# time.sleep(5)