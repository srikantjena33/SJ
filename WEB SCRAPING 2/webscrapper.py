from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/cameras/dslr~type/pr?sid=jek%2Cp31&otracker=nmenu_sub_Electronics_0_DSLR%20%26%20Mirrorless'

response = requests.get(url)
#print(response.status_code)
#print(response.content)

html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
#print(soup.prettify())

#print(soup.title)
#print(soup.title.text)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find('a'))

# for link in soup.find_all('a'):
#     print(link.get('href'))


# for image in soup.find_all('img'):
#     print(image.get('src'))

# product = soup.find_all('div',class_= '_4rR01T')
# print(product)

product = soup.find('div',attrs={'class': '_4rR01T'})
print(product)
    