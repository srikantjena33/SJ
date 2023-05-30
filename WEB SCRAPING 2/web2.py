from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/cameras/dslr~type/pr?sid=jek%2Cp31&otracker=nmenu_sub_Electronics_0_DSLR%20%26%20Mirrorless'


response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')


titles = []
prices = []
images = []

for item in soup.find_all('div',attrs={'class': '_2kHMtA'}):
    title = item.find('div',attrs={'class': '_4rR01T'})
    #print(title.string)
    
    price = item.find('div',attrs={'class': '_30jeq3 _1_WHN1'})
    #print(price.string)


    image = item.find('img',attrs={'class': '_396cs4'})
    #print(image.get('src'))

    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get('src'))
    
print(titles)
print(prices)
print(images)




