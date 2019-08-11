from django.test import TestCase

# Create your tests here.
import time
import requests
import json
from lxml import etree
from pyquery import PyQuery as pq
from stumanage.models import Movie
import datetime


url = "https://maoyan.com/board/4?offset=10"
response = requests.get(url).content
bod = str(response, encoding="utf-8")

html = etree.HTML(bod)
doc = pq(html)

movie_list = []
title = doc('dl dd')

def get_bod(num):
    url = "https://maoyan.com/board/4?offset={}".format(num)
    response = requests.get(url).content
    bod = str(response, encoding="utf-8")
    html = etree.HTML(bod)
    doc = pq(html)
    title = doc('dl dd')
    return title

def get_movie_list_dict(title):
    movie_list = []
    for i in range(0, 10):
        name = title.eq(i).find("p").eq(0).text()
        actor = title.eq(i).find("p").eq(1).text()[3:]
        up_time = title.eq(i).find("p").eq(2).text()[5:15]
        print(up_time)
        if len(up_time) < 6:
            up_time = up_time+'-'+"01-01"
        score = title.eq(i).find("p").eq(-1).text()
        img = title.eq(i).find("img").eq(1).attr("data-src")
        movie_list.append(Movie(**{
            "name": name,
            "actor": actor,
            "up_time": datetime.datetime.strptime(up_time, '%Y-%m-%d'),
            "score": score,
            "img": img
        }))
    return movie_list

def create_movie(movie_list):
    Movie.objects.bulk_create(movie_list)
    return "ok"

def main():
    for i in range(0, 91, 10):
        title = get_bod(i)
        movie_list = get_movie_list_dict(title)
        print(movie_list)
        create_movie(movie_list)

if __name__ == "__main__":
    main()