import requests
from bs4 import BeautifulSoup
from random import randint, choice

def random_compliment():
    page = randint(1,90)
    URL = f'http://kompli.me/komplimenty/page/{page}'
    print(page)

    request = requests.get(URL)
    scrap = BeautifulSoup(request.text, "html.parser")


    data_list = scrap.findAll("div", class_="post-card__description")

    compliment_list = [compliment.text.strip() for compliment in data_list if compliment.text != ""]
    print(compliment_list)
    return choice(compliment_list)