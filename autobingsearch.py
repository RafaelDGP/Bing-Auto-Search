import random
import time
import pyautogui
import keyboard

click_interval = 5

while True:
    current_x, current_y = pyautogui.position()
    pyautogui.click(current_x, current_y)
    time.sleep(click_interval)
    def get_list_of_words(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
        
    words = get_list_of_words('words.txt')
    random_word = random.choice(words)
    letter = list(random_word)
    output = random.sample(random_word, len(random_word))
    pyautogui.typewrite(output, interval=0.05)
    keyboard.send("enter")
    time.sleep(2)
    
    pyautogui.doubleClick(current_x, current_y)
    keyboard.send("backspace")
    
    time.sleep(1)
