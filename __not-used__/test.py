from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome('/Users/duckyounglee/Documents/chromedriver')

browser.get('https://cafe.naver.com/ArticleList.nhn?search.clubid=20486145&search.menuid=214&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.totalCount=501&search.cafeId=20486145&search.page=1')
browser.implicitly_wait(3)

login = browser.find_element_by_css_selector("a.gnb_btn_login")
login.click()

