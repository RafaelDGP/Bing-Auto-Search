# Bing-Auto-Search
This is a script designed to maximize your microsoft rewards points while being AFK. This script searches automatically in your Bing browser (or any other) with just one click. You can change the delay to search faster or slower.
# How to execute
## Execute these commands in the terminal:
`pip install pyautogui`
`pip install keyboard`
### Create a project in your compiler with the autobingsearch.py file and the words.txt file. Execute with your cursor on the bing search bar. 
# Customization
## You can change the delay for the first click and for the next search:
### First click:
`click_interval = [AMOUNT OF DELAY]`
### Line 26: Amount of time with the search open
`time.sleep([AMOUNT OF DELAY])`
### Line 32: Amount of time to write the next search
`time.sleep([AMOUNT OF DELAY])`
