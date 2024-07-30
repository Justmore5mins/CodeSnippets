from pinscrape.pinscrape import PinterestImageScraper
from sys import argv
state:bool = True
keywords:list[str] = []
while state:
    Input = input("Please enter keywords(enter \stop to stop):  ")
    if Input != "\stop":
        PinterestImageScraper().scrape(Input)
    else:
        state = False