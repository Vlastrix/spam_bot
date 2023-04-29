import pyautogui
from time import sleep
sleep(6)

def spam():
    f = open("spam_text.txt", "r", encoding="cp437")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


while True:
    spam()
