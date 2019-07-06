#app.py
from bs4 import BeautifulSoup as soup
import requests

from flask import Flask, request, json #import main Flask class and request object

my_url = 'https://short-edition.com/en/search/desires-engine'

app = Flask(__name__) #create the Flask app


@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        requestedTime = request.form.get('time')
        requestedTheme = request.form.get('theme')
        story_response = requests.post(my_url, data={"time":requestedTime, "theme": requestedTheme})
        if story_response.url != "https://short-edition.com/en/":
            story_page = story_response.text
            story_page_soup = soup(story_page, "html.parser")
            author = story_page_soup.find("div",{"class":"col-md-4 col-sm-4 col-xs-12 author-bloc"}).a.h2.get_text()
            story_name = story_page_soup.find("div",{"class":"titre-tag"}).h1.get_text()
            storyHTML = story_page_soup.find("div",{"class":"content"})
            strHTML = str(storyHTML)
            jsonINeedTosend = {
            "Author": author, "Title": story_name, "StoryHTML": strHTML
            }
            returnedJson =  json.dumps(jsonINeedTosend, ensure_ascii = False)
            return returnedJson
        else:
            story_response = requests.post(my_url, data={"time":requestedTime, "theme": requestedTheme})


        #return '''<h1>The time value is: {}</h1>
         #         <h1>The theme value is: {}</h1>'''.format(requestedTime, requestedTheme)
        

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000

