# Bing-Auto-Search
This is a script designed to maximize your microsoft rewards points while being AFK. This script searches automatically in your Bing browser (or any other) with just one click, you can change the delay to search faster or slower.

It works by writing for you a random combination of letters. 
> [!NOTE]
> Now Bing detects if you're actually writing, so many scripts do not work anymore, exept this one.
# How to execute
## Execute these commands in the terminal:
- `pip install pyautogui`
- `pip install keyboard`
Download both files and run the **autobingsearch.py** in your compiler
> [!NOTE]
> If it doesn't work, try putting both files in a folder and opening the folder in your compiler.

> [!IMPORTANT]
> **Execute with your cursor on the Bing search bar.**
# Customization
> [!NOTE]
> ## You can change the delay for the first click and for the next search:
> ### First click:
> - `click_interval = [SECONDS]`
> ### Line 26: Amount of time with the search open
> - `time.sleep([SECONDS])`
> ### Line 32: Amount of time to write the next search
> - `time.sleep([SECONDS])`
