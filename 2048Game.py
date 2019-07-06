from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()          # Uses Edge browser since mostly available on Windows 10
browser.get('https://play2048.co')                      # TODO: Add check if you beat high score
htmlElem = browser.find_element_by_tag_name('html')     # TODO: Add ability to retry game
while True:
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    scoreElem = browser.find_element_by_class_name('score-container')
    print("Score:", scoreElem.text.split('\n+')[0])   # Added split since + additions in score were showing

    if browser.find_elements_by_class_name('game-over'):
        print("Game over!")
        break
