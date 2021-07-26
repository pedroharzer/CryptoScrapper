from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()
driver.get("https://cointelegraph.com/tags/markets")
titles = []
def readMoreNews(btnClass):
    scrollNumber = 10
    for i in range(scrollNumber):
        try:
            print(i)
            time.sleep(3)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, btnClass))
            )
            element.click()
        except:
            print('a mimir')
            time.sleep(3)
            readMoreNews()
        finally:
            if i == scrollNumber - 1:
                return driver.page_source
def privacyPolicy(privacyBtnClass):
    cookies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, privacyBtnClass))
    )
    cookies.click()
def soupMess(titleTag, titleClass, privacyPolicyCheck = True):
    if privacyPolicyCheck:
        privacyPolicy('privacy-policy__accept-btn')
    soup = BeautifulSoup(readMoreNews('posts-listing__more-btn'), 'html.parser')
    sopa = soup.find_all(titleTag, titleClass)
    for itens in sopa:
        titles.append(itens.get_text())
    driver.quit()
    return titles