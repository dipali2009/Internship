#!/usr/bin/env python
# coding: utf-8

# # Q 1: Write a python program to display all the header tags from wikipedia.org.

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# # 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame

# In[11]:


from bs4 import BeautifulSoup
import requests
import re


url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]

ratings = [b.attrs.get('data-value')
    for b in soup.select('td.posterColumn span[name=ir]')]

votes = [b.attrs.get('data-value')
    for b in soup.select('td.ratingColumn strong')]

list = []

# create a empty list for storing
# movie information
list = []

# Iterating over movies to extract
# each movie's details
for index in range(0, 100):

    # Separating movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
    "year": year,
    "place": place,
    "star_cast": crew[index],
    "rating": ratings[index],
    "vote": votes[index],
    "link": links[index]}
    list.append(data)
print('\033[1m'+'IMDB’s Top rated 100 movies of all time'+'\033[0m')
# printing movie details with its rating.
for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
    ') -', 'Starring:', movie['star_cast'], movie['rating'])


# # 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[13]:


from bs4 import BeautifulSoup
import requests
import random
url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies
def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url

def imd_movie_picker():
    ctr=0
    print("--------------------------------------------")
    for movie in get_imd_movies('https://www.imdb.com/india/top-rated-indian-movies/'):
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        print(movie_title, movie_year)
        print("--------------------------------------------")
        ctr=ctr+1
        if (ctr==100):
          break;   
if __name__ == '__main__':
    imd_movie_picker()


# # 4) Write a python program to scrape product name, price and discounts from https://meesho.com/bagsladies/pl/p7vbp

# In[14]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
page=requests.get('https://meesho.com/bags-ladies/pl/p7vbp')
soup2=BeautifulSoup(page.content)
productnames1=[]
for i in soup2('div',class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"):
    productnames1.append(i.text)
prices1=[]
for i in soup2('div',class_="Card__BaseCard-sc-b3n78k-0 iLPHgK NewProductCard__PriceRow-sc-j0e7tu-5 eyya-Dr NewProductCard__PriceRow-sc-j0e7tu-5 eyya-Dr"):
    prices1.append(i.text)
discounts=[]
for i in soup2('img',class_="Card__BaseCard-sc-b3n78k-0 dpAIfg NewProductCard__BadgeRow-sc-j0e7tu-13 ezFwfg NewProductCard__BadgeRow-sc-j0e7tu-13 ezFwfg"):
    discounts.append(i.text)
df2=pd.DataFrame({'Product_Names':1,'Prices':prices1,'Discounts':discounts})
df2


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[15]:


team_details={'Team_ranking' :[],
               'Team_name' :[],
                'Matches' :[],
                'Points' :[],
                'Ratings' :[]}
#function call
print("Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.")
print("  ")
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'


page= requests.get(url)
soup=BeautifulSoup(page.text, 'html.parser')

ranking_table= soup.find('table' , class_='table')
    #print(ranking_table)


for rank in ranking_table.find_all('tbody'):
    rows = rank.find_all('tr')

    #selecting top 10 records only to display by rows[0:10]
    for row in rows[0:10]:

            #extracting all columns
        team_ranking= row.find_all('td')
        
            #strip() to remove extra spaces in string
        cols=[x.text.strip() for x in team_ranking] 
        
        #adding data to dictionary
        team_details['Team_ranking'].append(cols[0])
        #replacing \n in name by space
        team_details['Team_name'].append((cols[1]).replace('\n' ,' '))
        team_details['Matches'].append(cols[2])
        team_details['Points'].append(cols[3])
        team_details['Ratings'].append(cols[4])

        #print(team_details)
df=pd.DataFrame(team_details )
#to print dataframe without index
print(df.to_string(index=False))


# b) Top 10 ODI Batsmen along with the records of their team and rating.

# In[16]:


print("Top 10 ODI Batsmen along with the records of their team and rating.")
print("   ")

url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/ODI/batting'
bat= requests.get(url)

Batsman_details={'POS' :[],
               'PLAYER' :[],
                'TEAM' :[],
                'RATING' :[],
                'CAREER BEST RATING' :[]}


soup=BeautifulSoup(bat.text, 'html.parser')

data=soup.find('table',class_='table')
rows=data.find_all('tr')
for row in rows[1:11]:
    player_ranking = row.find_all('td')
    cols=[x.text.strip() for x in player_ranking]
 
    Batsman_details['POS'].append(cols[0])
                                  
    Batsman_details['PLAYER'].append(cols[1])
    Batsman_details['TEAM'].append(cols[2])
    Batsman_details['RATING'].append(cols[3])
    Batsman_details['CAREER BEST RATING'].append(cols[4])
    
df=pd.DataFrame(Batsman_details)

## to format string 1\n\n\n --> 1 

df["POS"]=df["POS"].str[:2]
df["POS"]=df["POS"].replace('\n','',regex=True) 
print(df)


# Top 10 ODI bowlers along with the records of their team and rating.

# In[17]:


url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'


page= requests.get(url)
soup=BeautifulSoup(page.text, 'html.parser')
table_body =soup.find('table')
row_data=[]
header_data=[]

for row in table_body.find_all('tr'):
    cols=row.find_all('td')
    col=[ele.text.strip() for ele in cols]

    row_data.append(col)
for headers in soup.find_all('th'):
    header=[headers.text.strip() ]
    header_data.append(header)

#ValueError: 1 columns passed, passed data had 5 columns getting this
#df=pd.DataFrame(row_data,columns=header_data) 

df=pd.DataFrame(row_data,columns=['POS','PLAYER','TEAM ','RATING','CAREER BEST RATING'])
df["POS"]=df["POS"].str[:2]
df["POS"]=df["POS"].replace('\n','',regex=True) 
df=df.dropna()
df.head(10)


# # 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape

# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating

# In[18]:


url='https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
page= requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table_body =soup.find('table')
row_data=[]
header_data=[]
i=0
for row in table_body.find_all('tr'):
    cols=row.find_all('td')
    col=[ele.text.strip() for ele in cols]
    
    
    row_data.append(col)
for headers in soup.find_all('th'):
    header=[headers.text.strip() ]
    header_data.append(header)

#ValueError: 1 columns passed, passed data had 5 columns getting this
#df=pd.DataFrame(row_data,columns=header_data) 

df=pd.DataFrame(row_data,columns=['Pos','Team','Matches','Points','Rating'])
df=df.replace('\n','  ',regex=True)
df2=df.dropna()
df2.head(10)


# b) Top 10 women’s ODI Batting players along with the records of their team and rating

# In[19]:


url='https://www.icc-cricket.com/rankings/womens/player-rankings/odi'
page= requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table_body =soup.find('table')
row_data=[]
header_data=[]

row_data_1=[] #to save 1st palyer data
row_data_1_rank=soup.find('span',class_='rankings-block__pos-number').text


row_data_1_name=soup.find('div',class_='rankings-block__banner--name').text

row_data_1_team=soup.find('div',class_='rankings-block__banner--nationality').text

row_data_1.append(row_data_1_rank.strip())
row_data_1.append(row_data_1_name.strip())
team_rate=row_data_1_team.split()

row_data_1.append(team_rate[0])
row_data_1.append(team_rate[1])

row_data.append(row_data_1)

for row in table_body.find_all('tr'):
    cols=row.find_all('td')
    col=[ele.text.strip() for ele in cols]
    
    row_data.append(col)
for headers in soup.find_all('th'):
    header=[headers.text.strip() ]
    header_data.append(header)

#ValueError: 1 columns passed, passed data had 5 columns getting this
#df=pd.DataFrame(row_data,columns=header_data) 

df=pd.DataFrame(row_data,columns=['Pos','Player','Team','Rating'])
df=df.replace('\n','  ',regex=True)
df2=df.dropna()
df2.head(10)


# In[ ]:


c) Top 10 women’s ODI all-rounder along with the records of their team and rating.


# In[20]:


url='https://www.icc-cricket.com/rankings/womens/player-rankings/odi'
page= requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
container=soup.find('div' , attrs={'data-title':"ODI All-Rounder Rankings" } )

table_body =container.find('table')


row_data=[]
header_data=[]

row_data_1=[] #to save 1st palyer dat

row_data_1_rank=container.find('span',class_='rankings-block__pos-number').text
row_data_1_name=container.find('div',class_='rankings-block__banner--name').text
row_data_1.append(row_data_1_rank.strip())
row_data_1.append(row_data_1_name.strip())

row_data_1_team=container.find('div',class_='rankings-block__banner--nationality').text

row_data_1.append(team_rate[0])
row_data_1.append(team_rate[1])

row_data.append(row_data_1)
i=0
for row in table_body.find_all('tr'):
    i=i+1
    cols=row.find_all('td')
    col=[ele.text.strip() for ele in cols]
    y=[]
    for x in col:
        if "This player has moved up" in x:
            x=x.replace('This player has moved up in the rankings since the previous rankings update','')
        elif 'This player has moved down' in x:
            x=x.replace('This player has moved down in the rankings since the previous rankings update','')
        y.append(x)    
       
    row_data.append(y)

for headers in soup.find_all('th'):
    header=[headers.text.strip()]
    header_data.append(header)
   
# ValueError: 1 columns passed, passed data had 5 columns getting this
#df=pd.DataFrame(row_data,columns=header_data) 
# del row_data[1]

df=pd.DataFrame(row_data,columns=['Pos','Player','Team','Rating'])
df=df.replace('\n' ,"" ,regex=True)
df=df.replace(' ' ,"" ,regex=True)
print(df.dropna())


# # 7) Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content and the code for the video from the link for the youtube video from the post.

# In[21]:


post_details ={'Heading':[],
                'Date':[],
                'Content':[],
                'Link':[]}
url=' https://www.coreyms.com.'
page = requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')

# ={'Heading':[]}

page_data=soup.find_all('header',class_="entry-header")
for x in page_data:
#extracting heading
    heading=x.find('h2',class_='entry-title').text
    post_details['Heading'].append(heading)
    
#extracting date
    date=x.find('time',class_='entry-time').text
    post_details['Date'].append(date)

page_content=soup.find_all('div', class_= 'entry-content')
 #to extract content
L=0
for i in page_content:
    L=L+1
    content=i.find('p').text
    post_details['Content'].append(content)
    
#to extract video link
#since 5th link is not present it shows none to skip 5th n iterate rest will have to enter blank string bcoz length of all sets has to be same in dict.
    if(L==5):
        link=""
        post_details['Link'].append(link)
        continue
    link=i.find('iframe' ,class_="youtube-player").get('src')
    post_details['Link'].append(link)
   # print(link)
    


df =pd.DataFrame(post_details)
df


# # 8) Write a python program to scrape house details from mentioned URL. It should include house title, location, area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, Rajaji Nagar.

# # 9) Write a python program to scrape mentioned details from dineout.co.in :
# 
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[29]:


page = requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
soup=BeautifulSoup(page.content)

name=[]
for i in soup.find_all("div", class_="restnt-info cursor"):
    name.append(i.text)
location=[]
for i in soup.find_all("div", class_="restnt-loc ellipsis"):
    location.append(i.text)

price = []
cuisine = []
for i in soup.find_all("span", class_="double-line-ellipsis"):
    price.append(i.text.split('|')[0])
    cuisine.append(i.text.split('|')[1])

rating=[]
for i in soup.find_all("div", class_="restnt-rating rating-3"):
    rating.append(i.text)
for i in soup.find_all("div", class_="restnt-rating rating-4"):
    rating.append(i.text)

images = []
for i in soup.find_all("img", class_="no-img"):
    images.append(i['data-src'])
    
print(len(name), len(location), len(price), len(cuisine), len(rating), len(images))

DineOut=pd.DataFrame({})
DineOut['Restaurant Name']=name
DineOut['Location']=location
DineOut['Price']=price 
DineOut['Cuisine']=cuisine  
DineOut['Rating']=rating  
DineOut['IMAGES']=images
DineOut


# # 10) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/women-tshirts?ga_q=tshirts .

# In[48]:


page=requests.get('https://www.bewakoof.com/women-tshirts?ga_q=tshirts')
soup1=BeautifulSoup(page.content)
productnames=[]
for i in soup1('div',class_="productCardDetail "):
    productnames.append(i.text)
prices=[]
for i in soup1('span',class_="discountedPriceText "):
    prices.append(i.text)
images_url=[]
for i in soup1('img',class_="productImgTag"):
    images_url.append(i["src"])
import pandas as pd
df1=pd.DataFrame({'Product_Names':productnames,'Prices':prices,'Images_url':images_url})
df1


# In[ ]:




