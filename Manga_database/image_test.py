import PIL
from PIL import Image
import requests
from io import BytesIO

response = requests.get("https://s8.mkklcdnv8.com/mangakakalot/j2/jq923321/chapter_14/1.jpg")
img = Image.open(BytesIO(response.content))

width, height = img.size

print(width, height)	