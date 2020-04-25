import sys
sys.stdout = open('/Users/MacBook/Desktop/powerball-master/powerball.txt', 'a')
import requests
from lxml import html
from selenium import webdriver
import datetime
chrome_path = r"/Users/MacBook/Desktop/chromedriver"
driver = webdriver.Chrome (chrome_path)
driver.get ("https://www.galottery.com/en-us/games/draw-games/powerball.html#tab-winningNumbers")
#driver.find_elements_by_xpath('''//*[@id="headerGameBannerInfo"]/div[2]/div[1]/span[1]/i''')[0].text
elems = driver.find_elements_by_xpath ("""//*[@id="winningNumbersSearchResults"]/table/tbody/tr[1]""") [0].text

print(elems.strip())

driver.close()
