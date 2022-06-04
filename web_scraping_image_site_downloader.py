import os
import requests
import bs4

url = "https://Imgur.com/search?q=python"
os.makedirs('Imgur', exist_ok=True)
res = requests.get(url)
res.raise_for_status()
img = bs4.BeautifulSoup(res.text, "html.parser")
link = img.select('.image-list-link')
comic_elem = img.select('')
if comic_elem == []:
    print('image could not be found!')
else:
    comic_url = 'https:' + comic_elem[0].get('src')
    res = requests.get(comic_url)
    res.raise_for_status()
    img_file = open(os.path.join('Imgur', os.path.basename(comic_url)))
    for chunk in res.iter_content(1000000):
        img_file.write(chunk)
    img_file.close()
print("Done!")
