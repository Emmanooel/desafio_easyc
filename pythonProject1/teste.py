import time
from selenium import webdriver 
from selenium.webdriver.common import by
from selenium.webdriver.common import keys

def bot():
    DRIVER_PATH = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    site = driver.get('https://best.aliexpress.com/?lan=en')

    procurar_item(driver)

def procurar_item(driver):
    driver.find_element('xpath', '//*[@id="search-key"]').send_keys('redmi')
    time.sleep(5)
    driver.find_element('xpath', '//*[@id="form-searchbar"]/div[1]/input').click()



if(__name__ == "__main__"):
    bot()