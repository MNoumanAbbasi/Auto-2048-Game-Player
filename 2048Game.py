from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()
browser.get('https://play2048.co')                      # TODO: Add check if you beat high score
htmlElem = browser.find_element_by_tag_name('html')
while True:
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    scoreElem = browser.find_element_by_class_name('score-container')
    print("Score:", scoreElem.text.split('\n+')[0])   # Added split since + additions in score were showing

