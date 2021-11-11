import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
base_url = "http://kamusi.appsmata.com"


def login(email, password):
    # Login to the website
    driver.get(f"{base_url}/login")
    time.sleep(5)
    driver.find_element_by_xpath(
        "/html/body/div/div[2]/div/div/div[1]/div/form/div[1]/div/input"
    ).send_keys(email)
    driver.find_element_by_xpath(
        "/html/body/div/div[2]/div/div/div[1]/div/form/div[2]/div/input"
    ).send_keys(password)

    print("Logged in")
    driver.find_element_by_xpath(
        "/html/body/div/div[2]/div/div/div[1]/div/form/div[4]/button"
    ).click()
    return driver


def get_soup(url):
    # Get the soup of the page
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    return soup


def generate_all_urls(max_page=833):
    # Generate all the urls
    urls = []
    for i in range(1, max_page + 1):
        urls.append(f"{base_url}/words?page={i}")
    return urls


def scrape_page(url):
    # Scrape the page
    soup = get_soup(url)
    table = soup.find_all("table")
    df = pd.read_html(str(table))[0]
    return df


def scrap_all_urls(urls):
    # Scrape all the urls
    all_df = []
    for url in urls:
        df = scrape_page(url)
        all_df.append(df)
    return all_df


if __name__ == "__main__":
    # Login to the website
    driver = login("email", "password")
    # Get the soup of the page
    urls = generate_all_urls()
    # Scrape all the urls
    all_df = scrap_all_urls(urls)
    # Combine all the dataframes
    df = pd.concat(all_df)
    # Save the dataframe
    df.to_csv("words.csv", index=False)
