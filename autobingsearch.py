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
    print(words)

    random_word = random.choice(words)
    letter = list(random_word)
    random.shuffle(letter)
    word = random_word + ''.join(letter) + random_word
    pyautogui.typewrite(word, interval=0.05)
    keyboard.send("enter")
    time.sleep(2)
    
    pyautogui.click(current_x, current_y)
    pyautogui.click(current_x, current_y)
    keyboard.send("backspace")
    
    time.sleep(2)