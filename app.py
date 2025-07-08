import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from random import choice
from flask import Flask, render_template



#Accumilation of quotes
quote_lst = []
base_url = "http://quotes.toscrape.com"
suffix = "/page/1"


while suffix:
    res = requests.get(f"{base_url}{suffix}")
    print(f"Scraping {base_url}{suffix} ......")
    soup = bs(res.text, "html.parser")
    quote_finder = soup.find_all(class_="quote")

    for q in quote_finder:
        quote_lst.append({"text":q.find(class_="text").get_text(),
        "author":q.find(class_="author").get_text(),
        "auth_info":q.find("a")["href"]})
        page_change = soup.find(class_="next")
    if page_change:
        suffix = page_change.find("a")["href"]
    else:
        suffix = None
    sleep(2)

app = Flask(__name__)

app.secret_key = "123"

@app.route("/")
def index():
    quote = choice(quote_lst)
    if len(quote["text"]) > 100:
        quote = choice(quote_lst)
    upt_guess = requests.get(f"{base_url}{quote['auth_info']}")
    soup1 = bs(upt_guess.text, "html.parser")
    bday_hint = soup1.find(class_="author-born-date").get_text()
    bplace_hint = soup1.find(class_="author-born-location").get_text()
    quote_text = quote["text"]
    return render_template("index.html", show_elements=True, quote_text=quote_text, quote=quote, bday_hint=bday_hint, bplace_hint=bplace_hint)
