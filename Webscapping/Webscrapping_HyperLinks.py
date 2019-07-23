#Webscrapping

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
URLLQ = 'https://www.lqgroup.org.uk/about/finance-performance-and-governance/financial-statements/'

urlNH = "https://www.nhhg.org.uk/publications/financial-statements/"

# Package the request, send the request and catch the response: r
r = requests.get(URLLQ)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))
    
