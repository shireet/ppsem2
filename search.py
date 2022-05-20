from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.chrome.options import Options
import time
import random

def make(ingredients):
    location_project = os.getcwd()
    chromeOptions = Options()
    chromeOptions = Options()
    chromeOptions.headless = True
    driver = webdriver.Chrome(location_project + "/chromedriver", options=chromeOptions)


    def open():
        driver.get('https://realfood.tesco.com/what-can-i-make-with.html')
        driver.implicitly_wait(3)

    def get_list(food, ingredients):
        for ing in ingredients:
            driver.find_element_by_xpath('//*[@id="ddl-recipe-finder"]/main/div[1]/div[1]/form/input').send_keys(ing)
            driver.find_element_by_xpath('//*[@id="ddl-recipe-finder"]/main/div[1]/div[1]/form/input').send_keys(Keys.ENTER)
        food = driver.find_elements_by_class_name("ddl-recipe-finder__list-item")
        return food

    def get_links(food):
        new = []
        for i in food:
            i.click()
            driver.switch_to.window(driver.window_handles[1])
            new.append(driver.current_url)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            if(len(new)>=10):
                break
        return new
    open()
    food = []
    food = get_list(food, ingredients)
    new = get_links(food)
    return new


