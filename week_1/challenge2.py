#code to create comic book
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from PIL import Image
from io import BytesIO

#empty lust to store scraped urls
image_urls=[]

#loop to go over each comic webpage, parse it and extract url of image
for page in range(1,2922):
    html=requests.get(f"https://xkcd.com/{page}/")
    comic_soup=SoupStrainer(id="comic")
    soup= BeautifulSoup(html.text, "lxml",parse_only=comic_soup)
    try:
        image_urls.append(soup.img['src'])
    except:
        continue

#download all images using the urls
images = [Image.open(BytesIO(requests.get("https:"+url).content)) for url in image_urls]

#save images to a pdf
pdf_path =r"c:\Users\olude\OneDrive\Documents\academics\stuff\The scrappy project\tsp_repository\week_1\ComicBook.pdf"
images[0].save(pdf_path, 'PDF', resolution=100.0, save_all=True, append_images=images[1:])

print("Comic Book created")