import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
# from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def autorisation(url, login, password):
    driver = webdriver.Chrome()
    driver.get(url)
    but_input = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div[2]/div[4]/button').click()
    time.sleep(1)

    email_input = driver.find_element(By.XPATH, '/html/body/div[5]/div/form/div[1]/input[1]')
    time.sleep(1)
    email_input.send_keys("AxeVal")
    time.sleep(1)

    paswd_input = driver.find_element(By.XPATH, '/html/body/div[5]/div/form/div[1]/input[2]')
    time.sleep(1)
    paswd_input.send_keys("4x3VaLve10")
    time.sleep(1)

    finish = driver.find_element(By.XPATH, '/html/body/div[5]/div/form/div[5]/div/button/div/span[1]').click()
    time.sleep(20)


def getNews(url):
    page = requests.get(url)

    filteredNews = []
    allNews = []

    soup = BeautifulSoup(page.text, "html.parser")

    allNews = soup.findAll('a', class_="card-full-news _parts-news")

    for data in allNews:
        filteredNews.append(data.find('h3', class_="card-full-news__title").text)

    for data in filteredNews:
        print(data, '\n')


def main():
    lenta_url = 'https://lenta.ru/parts/news/'
    getNews(lenta_url)

    osu_url = 'https://osu.ppy.sh/beatmapsets'
    autorisation(osu_url, 'AxeVal', '4x3VaLve10')


if __name__ == '__main__':
    main()
