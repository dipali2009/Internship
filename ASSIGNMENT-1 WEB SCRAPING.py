#!/usr/bin/env python
# coding: utf-8

# # 1) Write a python program to display all the header tags from wikipedia.org.

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[42]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


# In[43]:


html = urlopen('https://en.wikipedia.org/')


# In[44]:


bs = BeautifulSoup(html, "html.parser")


# In[45]:


titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])


# In[46]:


print('List all the header tags :', *titles, sep='\n\n')


# # Q2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[47]:


import pandas as pd
import re


# In[48]:


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


# # Q3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[49]:


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


# # 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm

# In[74]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[75]:


res=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
soup=BeautifulSoup(res.text,"html.parser")


# In[76]:


results = soup.find_all('div', attrs={'class':'presidentListing'})
results


# In[77]:


results[0]


# In[78]:


results[0].find('h3').text.strip("()")


# In[79]:


results[0].find('p').text.split(':',1)[1]


# In[80]:


presidents_info=[]


for r in range(len(results)):
    pname=results[r].find('h3').text.split('(',1)[0].strip()
    term=results[r].find('p').text.split(':',1)[1].strip()
    president_info ={"Name":pname,"Term of office":term}
    presidents_info.append(president_info)
    
presidents_info


# In[81]:


df=pd.DataFrame(presidents_info)
df


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape: a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[51]:


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


# # b) Top 10 ODI Batsmen along with the records of their team and rating.

# In[52]:


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


# # c) Top 10 ODI bowlers along with the records of their team and rating.

# In[53]:


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


# # Q6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape: a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating

# In[54]:


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


# # b) Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[55]:


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


# # c) Top 10 women’s ODI all-rounder along with the records of their team and rating.
# 

# In[56]:


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


# # 7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# i) Headline
# ii) Time
# iii) News Link

# In[82]:


from bs4 import BeautifulSoup
import re
import requests
import pandas as pd


# In[83]:


req=requests.get('https://www.cnbc.com/world/?region=world')
soup=BeautifulSoup(req.text,"html.parser")


# In[84]:


result=soup.find_all('li',attrs={'class':'LatestNews-item'})
#result


# In[85]:


result[0]


# In[86]:


result[0].find('time').text
result[0].find('a').text
result[0].find('a')['href']


# In[87]:


news_info=[]

for r in range(len(result)):
    headline=result[r].find('a').text.strip()
    time=result[r].find('time').text.strip()
    news_link=result[r].find('a')['href']
    news={'HeadLine':headline,'Time':time,'News Link':news_link}
    news_info.append(news)
    
news_info


# In[88]:


df=pd.DataFrame(news_info)
df


# # Q8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days. https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details :
# i) Paper Title 
# ii) Authors
# iii) Published Date 
# iv) Paper URL 
# 

# In[89]:


from bs4 import BeautifulSoup
import re
import requests
import pandas as pd


# In[98]:


req=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
soup=BeautifulSoup(req.text,"html.parser")


# In[106]:


result=soup.find_all('li',attrs={'class':'sc-9zxyh7-1 sc-9zxyh7-2 exAXfr jQmQZp'})
#result


# In[107]:


result[0]


# In[101]:


print(result[0].find('span',class_='sc-1thf9ly-2 bKddwo').text)
print(result[0].find('span',class_='sc-1w3fpd7-0 pgLAT').text)
print(result[0].find('a').text)
print(result[0].find('a')['href'])


# In[102]:


articles_info=[]

for r in range(len(result)):
    title=result[r].find('a').text.strip()
    authors=result[r].find('span',class_='sc-1w3fpd7-0 pgLAT').text.strip()
    pdate=result[r].find('span',class_='sc-1thf9ly-2 bKddwo').text.strip()
    paper_url=result[r].find('a')['href']
    article={'Paper Title':title,'Authors':authors,'Published Date':pdate,'Paper URL':paper_url}
    articles_info.append(article)
    
articles_info


# In[103]:


df=pd.DataFrame(articles_info)
df


# # Q 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location 
# iv) Ratings
# v) Image URL

# In[108]:


req=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
soup=BeautifulSoup(req.text,"html.parser")


# In[109]:


result=soup.find_all('div',attrs={'class':'restnt-card restaurant'})
#result


# In[110]:


result[0]


# In[111]:


print(result[0].find('div',class_='restnt-rating rating-4 hide').text)
print(result[0].find('img')['data-src'])
print(result[0].find('a').text)
#print(result[0].find('span').find_all('a')[0].text)

foods=[]
for i in result[0].find('span').find_all('a'):
    foods.append(i.text)
    
print(','.join(foods))

loc_info=[]
for j in result[0].find('div',class_='restnt-loc ellipsis').find_all('a'):
    loc_info.append(j.text)
    
print(','.join(loc_info))


# In[112]:


restaurant_info=[]

for r in range(len(result)):
    res_name=result[r].find('a').text.strip()
    foods=[]
    for i in result[r].find('span').find_all('a'):
        foods.append(i.text)
    cuisine=','.join(foods)
    loc_info=[]
    for j in result[r].find('div',class_='restnt-loc ellipsis').find_all('a'):
        loc_info.append(j.text)
    location=','.join(loc_info)
    rating=result[r].find('div',class_='restnt-rating rating-4 hide').text
    image_url=result[r].find('img')['data-src']
    restaurant={'Restaurant name':res_name,'Cuisine':cuisine,'Location':location,'Ratings':rating,'Image URL':image_url}
    restaurant_info.append(restaurant)
    
restaurant_info


# In[113]:


df=pd.DataFrame(restaurant_info)
df


# In[ ]:




