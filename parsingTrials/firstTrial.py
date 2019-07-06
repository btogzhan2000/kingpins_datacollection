from bs4 import BeautifulSoup as soup
from newspaper import Article
import requests

from flask import Flask, request, json


#yandex_url = f"https://yandex.kz/search/?text=\{searched_item}%20url%3A{web_site_choice}%2F*&lr=162%within={time_within_dictionary}&p={page_num}"




'''"First Trail Of Using Standard Libraries to Extract Articles From Websites"
url = "https://tengrinews.kz/kazakhstan_news/ERG-pervoy-promyishlennyih-kompaniy-kazahstane-podderjala-370533/"
article = Article(url, language='ru')

article.download()
article.parse()
print(article.text)
article.nlp()'''
#new comment



#send to yandex to find relevant material
time_within_dictionary = {"6-month": "4", "1-year":"5", "day": "77", "1-month": "2"}
web_site_choice = "https://tengrinews.kz"

#get by post and space should be raplaced with +
searched_item = "through+request"
#yandex_url = f"https://yandex.kz/search/?text=\{searched_item}%20url%3A{web_site_choice}%2F*&lr=162%within={time_within_dictionary}&p={page_num}"


"""def urlGetter101(website_url, alist):
    search_page = requests.get(website_url).text
    search_page_soup = soup(search_page, "html.parser")
    url_container = search_page_soup.findAll("div",{"class": "organic typo typo_text_m typo_line_s"})
    for link in url_container:
        x = link.h2.a["href"]
        #check for valid urls and avoid adds
        #if x.startswith(web_site_choice):
        alist.append(link.h2.a["href"])"""
search_page = requests.get("https://yandex.kz/search/?text=ERG%20url%3Ahttps%3A%2F%2Ftengrinews.kz%2F*&lr=162%25within%3D2&p=0")
search_page_soup = soup(search_page.content, "html.parser")
print(search_page_soup)
url_container = search_page_soup.findAll("a",{"class": "link link_theme_normal organic__url link_cropped_no i-bem"})
#print(url_container)


#urlGetter101("https://yandex.kz/search/?text=ERG%20url%3Ahttps%3A%2F%2Ftengrinews.kz%2F*&lr=162%25within%3D2&p=0", urllist)



"""for link in search_page_soup.findAll("div",{"class":"organic typo typo_text_m typo_line_s"}):
        print(link.h2.a["href"])"""

'''def urlGetter(website, alist):
    """search_page = requests.get(website + "0").text
    search_page_soup = soup(search_page, "html.parser")
    x = search_page_soup.find("div",{"class": "serp-adv__found"})"""


    needed_url_containers = []
    for n in range(0,19):
        search_page = requests.get(website + str(n))
        search_page_soup = soup(search_page, "html.parser")
        """for link in search_page_soup.findAll("div",{"class":"organic typo typo_text_m typo_line_s"}):
        print(link.h2.a["href"])"""
        needed_url_containers.append(search_page_soup.find("div",{"class":"organic typo typo_text_m typo_line_s"}))
    for container_pages in story_url_containers:
        for container in container_pages:
            storyUrl = baseUrl + container.h2.a["href"]
            alist.append(storyUrl)'''





#go to each found link and parse the article
article_urls = []


#then check whether we have wanted words in artice, if not then we stop our process of parsing.


