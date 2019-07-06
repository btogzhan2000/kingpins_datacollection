from bs4 import BeautifulSoup as soup
import html2text
import requests

import csv

my_url = 'https://short-edition.com/en/'
baseUrl = 'https://short-edition.com'
categoryUrls = []
one_min_urls = []
three_min_urls = []
five_min_urls = []
classic_urls = []
story_url_containers = [] 

filename = "stories.csv"
f = open(filename, "w")
headers = "Author, Category, Name, Content\n"
f.write(headers)



def urlGetter(website, alist):
    for n in range(1,19):
        category_page = requests.get(website + str(n)).text
        category_page_soup = soup(category_page, "html.parser")
        story_url_containers.append(category_page_soup.findAll("div",{"class":"js-infinite-scroll-content"}))
    for container_pages in story_url_containers:
        for container in container_pages:
            storyUrl = baseUrl + container.h2.a["href"]
            alist.append(storyUrl)

def story_getter(one_array_of_urls):
    for url in one_array_of_urls:
        
        story_page = requests.get(url).text
        story_page_soup = soup(story_page, "html.parser")
        
        author = story_page_soup.find("div",{"class":"col-md-4 col-sm-4 col-xs-12 author-bloc"}).a.h2.get_text()
        category = story_page_soup.find("div",{"class":"ariane hidden-xs hidden-sm"}).findAll("a")[1].get_text()
        story_name = story_page_soup.find("div",{"class":"titre-tag"}).h1.get_text()
        storyHTML = story_page_soup.find("div",{"class":"content"})
        thewriter.writerow({"Category": category, "Author": author, "Name":story_name, "Content": story})
        
        #storyInQuotes = "\"" + story + "\""
        authorInQuotes = "\"" + author + "\""
        storyNameInQuotes = "\"" + story_name + "\""
        
        #storyInQuotes = "\""+ story_text + "\""
        #print(storyInQuotes)
        
        f.write(category + ","+ authorInQuotes + "," + storyNameInQuotes + "," + story +"\n")


urlGetter('https://short-edition.com/en/category/1-min?page=', one_min_urls)
urlGetter('https://short-edition.com/en/category/3-min?page=', three_min_urls)
urlGetter('https://short-edition.com/en/category/5-min?page=', five_min_urls)
urlGetter('https://short-edition.com/en/category/classic?page=', classic_urls)





with open("new_stories.csv","w",newline = '') as f:
    fieldnames = ["Category", "Author", "Name", "Content"]

    thewriter = csv.DictWriter(f, fieldnames = fieldnames)
    thewriter.writeheader()

    story_getter(one_min_urls)
    story_getter(three_min_urls)
    story_getter(five_min_urls)
    story_getter(classic_urls)



