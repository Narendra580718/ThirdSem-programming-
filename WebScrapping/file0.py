import requests
from bs4 import BeautifulSoup

url="https://softwarica.edu.np/"

#STEP: 1
r=requests.get(url)
print(r)
print(r.status_code)
print(r.url)
htmlcontent=(r.content)
print(htmlcontent)

#STEP: 2
soup=BeautifulSoup(htmlcontent, 'html.parser')
print(soup.prettify())
print(soup.title)

#STEP: 3 HTML tree Traversal
#Commonly used types of objects:
print(type(soup.title)) #1.Tag
print(type(soup.title.string))#2.NavigableString
print(soup)#3.BeautifulSoup

#4.Comment
#Get all the comments in the html page
markup = '<p><!--This is a comment-></p>'
soup2=BeautifulSoup(markup)
print(soup2.p) #<p><!--This is a comment
print(soup2.p.string)#This is a comment
print(type(soup2.p.string))#<class 'bs4.element.Comment

#Get the title of the html page
title= soup.title
print(title)
print(type(title))
print(title.string)
print(type(title.string))

#Get the first paragraph from the page
print(soup.find('p'))

#Get all the paragraphs from the page
paragraph=soup.find_all('p')
print(paragraph)

# Get all the anchor tags from the page
print(soup.find_all('a'))

# Getting the title tag
print(soup.title)

# Getting the name of the tag
print(soup.title.name)

# Getting the name of parent tag
print(soup.title.parent.name)

#Get all the text from the html page
print(soup.get_text())

#Get the texts from the tag/soup
print(soup.find('p').get_text())

#Get classes of any element in the html page
print(soup.find('p')['class']) #['mt-2', 'text-sm', 'text-gray-500', 'md:textbase']

#Get classes of any element in the html page
print(soup.find('p')['class'])

# Find all the elements with class mt-2
print(soup.find_all("p",class_="mt-2"))

# Get all anchors tag from the page
anchors=soup.find_all('a')
print(anchors)
all_links=set()

#Get all the links on the page
for link in anchors:

    if(link.get('href') !='#'):

        linkText ='https://url'+ link.get('href')
        all_links.add(link)
        print(linkText)

