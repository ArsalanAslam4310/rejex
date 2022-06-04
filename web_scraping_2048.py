from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.page_load_strategy = 'eager'
browser = webdriver.Firefox(options=options)
browser.maximize_window()
browser.get('https://gabrielecirulli.github.io/2048/')
game_container = browser.find_element_by_tag_name('html')
browser.stop_client()
game_container.click()

while True:
    game_container.send_keys(Keys.UP)
    game_container.send_keys(Keys.DOWN)
    game_container.send_keys(Keys.LEFT)
    game_container.send_keys(Keys.RIGHT)
    try:
        if browser.find_element_by_class_name('game-over'):
            break
    except:
        continue
browser.quit()
