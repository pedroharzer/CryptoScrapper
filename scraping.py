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
    scrollNumber = 1 #times you want to click more news button
    for i in range(scrollNumber):
        try:
            print(i)
            time.sleep(3)
            element = WebDriverWait(driver, 10).until( #waits untin the more news button appears
                EC.presence_of_element_located((By.CLASS_NAME, btnClass))
            )
            element.click()
        except:
            print('a mimir')
            time.sleep(3)
            readMoreNews() #calls it self again if it fails to find the button
        finally:
            if i == scrollNumber - 1: #after the set number of scrols, it returns the full page source
                return driver.page_source
def privacyPolicy(privacyBtnClass): #skips cookies
    cookies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, privacyBtnClass))
    )
    cookies.click()
def getLinks(): #get all links in the news feed
    linkList = []
    privacyPolicy('privacy-policy__accept-btn') #cookie skip
    soup = BeautifulSoup(readMoreNews('posts-listing__more-btn'), 'html.parser')
    links = soup.find_all('a', 'post-card-inline__title-link') #get all news links
    for link in links:
        linkList.append(link.get('href'))
    return linkList
def soupMess(titleTag, titleClass, privacyPolicyCheck = True): #gets and filters all titles
    if privacyPolicyCheck:
        privacyPolicy('privacy-policy__accept-btn')
    soup = BeautifulSoup(readMoreNews('posts-listing__more-btn'), 'html.parser')
    sopa = soup.find_all(titleTag, titleClass)
    for itens in sopa:
        titles.append(itens.get_text())
    driver.quit()
    return titles
def getFullPage(links): #go news by news and return each page source as an array
    allHtmls = []
    for link in links:
        driver.get("https://cointelegraph.com" + str(link))
        allHtmls.append(driver.page_source)
    return allHtmls
def getTextFromPage(sources): #get all the text from each page and return an array with it all good to go
    allTexts = []
    filteredTexts= []
    fullTxt = ''
    for source in sources:
        soup = BeautifulSoup(source, 'html.parser')
        p = soup.find_all('p')
        for e in p:
            if e.find(class_ = 'post-content__disclaimer'):
                p.pop()
            else:
                allTexts.append(e.get_text())
        for filteredText in allTexts:
            fullTxt = filteredText + ' '
        print(filteredTexts) #filtered txt showing only last one
        filteredTexts.append(fullTxt)
        fullTxt = ''
        allTexts = []
    return filteredTexts
source = getFullPage(getLinks())
print(getTextFromPage(source))

