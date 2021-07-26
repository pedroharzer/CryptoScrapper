from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()
driver.get("https://cointelegraph.com/tags/markets")
titles = []
def getHtml():
    html = driver.page_source
    driver.quit()
    return html

def newGetHtml():
    scrollNumber = 10
    for i in range(scrollNumber):
        try:
            print(i)
            time.sleep(3)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'posts-listing__more-btn'))
            )
            element.click()
        except:
            print('a mimir')
            time.sleep(3)
            newGetHtml()
        finally:
            if i == scrollNumber - 1:
                return driver.page_source
def privacyPolicy():
    try:
        cookies = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'privacy-policy__accept-btn'))
        )
        cookies.click()
    finally:
        try:
            driver.find_element_by_class_name("privacy-policy__text")
        except:
            try:
                cookies = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "container privacy-policy__wrp"))
        )
            except:
                return True
def soupMess():
    privacyPolicy()
    soup = BeautifulSoup(newGetHtml(), 'html.parser')
    sopa = soup.find_all('span', 'post-card-inline__title')
    for itens in sopa:
        titles.append(itens.get_text())
    driver.quit()
    return titles