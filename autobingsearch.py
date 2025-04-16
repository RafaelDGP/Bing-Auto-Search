import random
import time
import pyautogui
import keyboard

click_interval = 5
active = False
close = False

def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

words = get_list_of_words('words.txt')

print("Press 'Q' to start and 'E' to stop")

while True:
    # Starts bot
    if keyboard.is_pressed('q') and not active:
        active = True
        time.sleep(0.5)

    if active:
        # Checks if user wants to stop before act
        if keyboard.is_pressed('e'):
            active = False
            time.sleep(0.5)
            continue

        # Execute automatic tasks
        current_x, current_y = pyautogui.position()
        pyautogui.click(current_x, current_y)

        # While wait, checks if needs to stop
        for _ in range(int(click_interval * 10)):
            if keyboard.is_pressed('e'):
                active = False
                time.sleep(0.5)
                break
            time.sleep(0.1)
        if not active:
            continue

        # Chooses a random word from the words.txt file and scrambles the chosen word, then press enter.
        random_word = random.choice(words)
        scrambled = random.sample(random_word, len(random_word))
        pyautogui.typewrite(scrambled, interval=0.05)
        keyboard.send("enter")

        for _ in range(20):
            if keyboard.is_pressed('e'):
                active = False
                time.sleep(0.5)
                break
            time.sleep(0.1)
        if not active:
            continue

        # Select all text and exclude
        pyautogui.doubleClick(current_x, current_y)
        keyboard.send("backspace")

        for _ in range(10):
            if keyboard.is_pressed('e'):
                active = False
                time.sleep(0.5)
                break
            time.sleep(0.1)
