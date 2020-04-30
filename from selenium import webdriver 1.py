import sys
sys.stdout = open('/Users/MacBook/Desktop/powerball-master/powerball.txt', 'a')
import requests
from lxml import html
from selenium import webdriver
import datetime

chrome_path = r"/Users/MacBook/Desktop/chromedriver"
driver = webdriver.Chrome (chrome_path)
driver.get ("https://www.galottery.com/en-us/games/draw-games/powerball.html#tab-winningNumbers")
elems_date = driver.find_elements_by_xpath ("""//*[@id="headerGameBannerInfo"]/div[1]/time""") [0].text
elems_num1 = driver.find_elements_by_xpath ("""//*[@id="headerGameBannerInfo"]/div[2]/div[1]/span[1]/i""") [0].text
elems_num2 = driver.find_elements_by_xpath ("""//*[@id="headerGameBannerInfo"]/div[2]/div[1]/span[2]/i""") [0].text
elems_num3 = driver.find_elements_by_xpath ("""//*[@id="headerGameBannerInfo"]/div[2]/div[1]/span[3]/i""") [0].text
elems_num4 = driver.find_elements_by_xpath ("""//*[@id="headerGameBannerInfo"]/div[2]/div[1]/span[4]/i""") [0].text
elems_num5 = driver.find_elements_by_xpath ("""//*[@id="headerGameBannerInfo"]/div[2]/div[1]/span[5]/i""") [0].text
elems_powerball = driver.find_elements_by_xpath ("""//*[@id="headerGameBannerInfo"]/div[2]/div[1]/span[6]/i""") [0].text
elems_multiplyer = driver.find_elements_by_xpath ("""//*[@id="winningNumbersSearchResults"]/table/tbody/tr[1]/td[2]/div/span[7]/i""") [0].text


print(elems_date.strip(), end = ' ')
print(elems_num1.strip(), end = ' ')
print(elems_num2.strip(), end = ' ')
print(elems_num3.strip(), end = ' ')
print(elems_num4.strip(), end = ' ')
print(elems_num5.strip(), end = ' ')
print(elems_powerball.strip(), end = ' ')
print(elems_multiplyer.strip(), end = ' ')


driver.close()
