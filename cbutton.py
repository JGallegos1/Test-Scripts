from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v2.html')

browser.maximize_window()

eightButton = browser.find_element_by_name('eight')
nineButton = browser.find_element_by_name('nine')
count = 0
while(count < 16):
    eightButton.click()
    time.sleep(.4)
    count = count +1

nineButton.click()

time.sleep(2)

cButton = browser.find_element_by_name('clear')
cButton.click()
