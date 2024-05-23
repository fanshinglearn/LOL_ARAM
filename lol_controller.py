import pyautogui
import pydirectinput

pyautogui.FAILSAFE = True

class LOL:
    # 右鍵
    @staticmethod
    def walk(pos: tuple):
        pyautogui.mouseDown(pos, button="right")
        pyautogui.mouseUp(button="right")

    # 左鍵
    @staticmethod
    def click(pos: tuple):
        pyautogui.mouseDown(pos)
        pyautogui.mouseUp()

    # 快捷攻擊型移動
    @staticmethod
    def attack(pos: tuple, attack_key: str = 't'):
        pyautogui.moveTo(pos)
        pydirectinput.press(attack_key)
