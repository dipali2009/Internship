#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


# importing necessary Library

import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


# Q1) Scrape the details of most viewed videos on YouTube from Wikipedia.
# Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos
# You need to find following details:
# A) Rank
# B) Name
# C) Artist
# D) Upload date
# E) View

# In[3]:


# getting web driver
driver=webdriver.Chrome(r'C:\Users\Acer\Downloads\chromedriver_win32\chromedriver.exe')


# In[4]:


# getting the web page
url= "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"
driver.get(url)
time.sleep(3)


# In[25]:


# Creating empty list for scaping the data

Rank = []
Name = []
Artist = []
Upload_Date = []
Views = []


# In[26]:


# Scraping Rank of the videos
try:
    for i in driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[1]'):
        Rank.append(i.text)
except NoSuchElementException:
    Rank.append("_")


# In[27]:


# Scraoing Name of the videos
try:
    for i in driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[2]'):
        Name.append(i.text)
except NoSuchElementException:
    Name.append("_")


# In[28]:


# Scraping Artist of the video
try:
    for i in driver.find_elements(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[3]"):
        Artist.append(i.text)
except NoSuchElementException:
    Artist.append("_")


# In[29]:


# Scraping Uploaded date of the video
try:
    for i in driver.find_elements(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[4]"):
        Upload_Date.append(i.text)
except NoSuchElementException:
    Upload_Date.append("_")


# In[30]:


# Scraping Views of videos
try:
    for i in driver.find_elements(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[5]"):
        Views.append(i.text)
except NoSuchElementException:
    Views.append("_")


# In[31]:


# Creating DataFrame fr scraped data
YouTube = pd.DataFrame({})
YouTube['Rank']=Rank
YouTube['Name']=Name
YouTube['Artist']=Artist
YouTube['Upload Date']=Upload_Date
YouTube['Views']=Views


# In[32]:


YouTube


# Q2. Scrape the details team India’s internationalfixtures from bcci.tv. 
# Url = https://www.bcci.tv/.
# You need to find following details:
# A) Match title (I.e. 1stODI)
# B) Series
# C) Place
# D) Date
# E) Time
# Note: - From bcci.tv home page you have reach to the international fixture page through code.

# In[7]:


# Getting the webpage of mentioned url 
url=('https://www.bcci.tv/')
driver.get(url)


# In[9]:


#finding menu button and click on it
menu_tag=driver.find_element(By.XPATH,'//*[@id="nav-main"]/div[1]')
menu_tag.click()


# In[10]:


# finding international icon on bar and click on it
internation_icon= driver.find_element(By.XPATH,'/html/body/nav/div[1]/div[2]/ul[1]/li[2]/a')
internation_icon.click()


# In[11]:


#finding fixtures and click on it
fixture_icon=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/ul/li[1]/a')
fixture_icon.click()


# In[12]:


# finding the web element and scrape the details for match title and place
match_title=[]
place=[]


m_place_tag=driver.find_elements(By.XPATH, '//div[@class="fix-place ng-binding ng-scope" ]')
for i in m_place_tag:
    match_title.append((i.text).split('-')[0])
    place.append((i.text).split('-')[1])
print(len(match_title),len(place))


# In[13]:


# finding web element and scrape the date
date=[]

date_tag=driver.find_elements(By.XPATH,'//h5[@class="ng-binding"]')
for i in date_tag:
    date.append(i.text)
len(date)


# In[14]:


time=[]

time_tag=driver.find_elements(By.XPATH,'//h5[@class="text-right ng-binding"]')
for i in time_tag:
    time.append(i.text)
time


# In[15]:


# finding web element and scape series details
series=[]
temp=[]
series_tag=driver.find_elements(By.XPATH,'//h5[@class="fix-text"]')
for i in series_tag:
    temp.append(i.text)
for i in range(1,len(temp),2):
    series.append(temp[i])
series


# In[16]:


# scape title of the match
title=[]
title_tag=driver.find_elements(By.XPATH,'//div[@class="fixture-card-mid d-flex align-items-center justify-content-between"]')
for i in title_tag:
    title.append((i.text).replace('\n', ' '))
title


# In[17]:


#let's prepare Dataframe

bcci_tv= pd.DataFrame({'Series':series, 'Match Title': title, 'Matches':match_title, 
                       'Date': date, 'Time': time, 'Place': place})

print("\nUpcoming International Fixtures ")
bcci_tv


# In[18]:


driver.close()


# Q3. Scrape the details of State-wise GDP ofIndia fromstatisticstime.com. 
# Url = http://statisticstimes.com/
# You have to find following details:
# A) Rank
# B) State
# C) GSDP(18-19)- at current prices
# D) GSDP(19-20)- at current prices
# E) Share(18-19)
# F) GDP($ billion)
# Note: - From statisticstimes home page you have to reach to economy page through code

# In[20]:


# getting web driver
driver=webdriver.Chrome(r'C:\Users\Acer\Downloads\chromedriver_win32\chromedriver.exe')


# In[21]:


# getting the web page
url=' http://statisticstimes.com/'
driver.get(url)


# In[30]:


#find economy drop button and click on it
economy_tag=driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]')
economy_tag.click()

india_tag=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
india_tag.click()


# In[31]:


# find India GDP and click on it
india_gdp=driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
india_gdp.click()


# In[32]:


# finding web elements and scrape the details of all the required field
rank=[]
rank_tag=driver.find_elements(By.XPATH, '//td[@class="data1"]')
for i in rank_tag[:33]:
    rank.append(i.text)
len(rank)


# In[33]:


state=[]
state_tag=driver.find_elements(By.XPATH, '//td[@class="name"]')
for i in state_tag[:33]:
    state.append(i.text)
len(state)


# In[34]:


gsdp18_19= []
gsdp_tag= driver.find_elements(By.XPATH,'//td[@class="data sorting_1"]')
for i in gsdp_tag[:33]:
    gsdp18_19.append(i.text)
len(gsdp18_19)


# In[35]:


share=[]
share_tag=driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div[5]/div[1]/div/table/tbody/tr/td[5]')
for i in share_tag:
    share.append(i.text)
    
len(share)


# In[36]:


gsdp19_20=[]
gsdp19_tag=driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div[5]/div[1]/div/table/tbody/tr/td[3]')
for i in gsdp19_tag:
    gsdp19_20.append(i.text)
len(gsdp19_20)


# In[37]:


gdp_bill=[]
gdp_tag=driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div[5]/div[1]/div/table/tbody/tr/td[6]')
for i in gdp_tag:
    gdp_bill.append(i.text)
len(gdp_bill)


# In[38]:


len(rank),len(state), len(gsdp18_19), len(gsdp19_20), len(share),len(gdp_bill)


# In[40]:


# preparing the data frame
GDP_states= pd.DataFrame({'Rank':rank, 'State':state, 'GSDP 18-19':gsdp18_19, 'GSDP 19-20':gsdp19_20,
                         'Share 18-19':share, 'GDP ($ Billion)':gdp_bill})
print("Indian States by GDP\n")
GDP_states


# In[41]:


driver.close()


# QScrape the details of top 100 songs on billiboard.com. 
# Url = https:/www.billboard.com/
# You have to find the following details:
# A) Song name
# B) Artist name
# C) Last week rank
# D) Peak rank
# E) Weeks on board
# Note: - From the home page you have to click on the charts option then hot 100-page link through code.
# 

# In[61]:


# getting web driver
driver=webdriver.Chrome(r'C:\Users\Acer\Downloads\chromedriver_win32\chromedriver.exe')


# In[63]:


url=("https://www.billboard.com")
driver.get(url)


# In[66]:


#Clicking on hot 100
Search=driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/h3/a").get_attribute('href')
driver.get(Search)


# In[71]:


#web element for song title
xyz_tag=driver.find_elements(By.ID, "title-of-a-story")
xyz=[]
for i in xyz_tag:
    xyz.append(i.text)
len(xyz)


# In[72]:


# scraping meaningful data, here songs from scarpe data
song = list(filter (lambda k: k!= '', xyz))
song=song[:100]


# In[73]:


len(song)


# In[74]:


# scrape web elemnt for artist and scrape the details
artist=[]
art_tag= driver.find_elements(By.XPATH,'/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div/ul/li[4]/ul/li[1]/span')
for i in art_tag:
    artist.append(i.text)
len(artist)


# In[75]:


# find web elements of all the required field and scrape them.
last_rank=[]
last_tag=driver.find_elements(By.XPATH, '/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div/ul/li[4]/ul/li[7]/ul/li[3]')
for i in last_tag:
    last_rank.append(i.text)
len(last_rank)


# In[76]:


peak_rank=[]
peak_tag=driver.find_elements(By.XPATH,'/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div/ul/li[4]/ul/li[7]/ul/li[4]/span')
for i in peak_tag:
    peak_rank.append(i.text)
len(peak_rank)


# In[77]:


weeks_on=[]
w_board_tag=driver.find_elements(By.XPATH, '/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div/ul/li[4]/ul/li[7]/ul/li[5]/span')
for i in w_board_tag:
    weeks_on.append(i.text)
len(weeks_on)


# In[78]:


# preparing dataframe
hot_100= pd.DataFrame({'Song Title':song, 'Artist':artist, 'Last week Rank':last_rank, 'Peak Rank':peak_rank,
                     'Weeks On Board':weeks_on})
print("Hot 100 in BillBoard\n")
hot_100


# In[79]:


driver.close()


# Q.6 Scrape the details of Highest sellingnovels.
# Url = https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-greycompare/
# You have to find the following details:
# A) Book name
# B) Author name
# C) Volumes sold
# D) Publisher
# E) Genre

# In[80]:


# getting web driver
driver=webdriver.Chrome(r'C:\Users\Acer\Downloads\chromedriver_win32\chromedriver.exe')


# In[81]:


# getting the web page
url= 'https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare'
driver.get(url)


# In[82]:


# finding the web element of all the required details and scrape them.
book=[]
book_tag=driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[2]')
for i in book_tag:
    book.append(i.text)
len(book)


# In[83]:


author=[]
author_tag=driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[3]')
for i in author_tag:
    author.append(i.text)
len(author)


# In[84]:


volume=[]
sold_tag=driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[4]')
for i in sold_tag:
    volume.append(i.text)
len(volume)


# In[85]:


publisher=[]
publish_tag=driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[5]')
for i in publish_tag:
    publisher.append(i.text)
len(publisher)


# In[86]:


genre=[]
genre_tag=driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[6]')
for i in genre_tag:
    genre.append(i.text)
len(genre)


# In[87]:


len(book), len(author), len(volume),len(publisher), len(genre)


# In[88]:


# preparing Dataframe
Novels=pd.DataFrame({'Book Title':book, 'Author':author, 'Volume Sales':volume,
                    'Publisher':publisher, 'Genre':genre})
print("List of Highest Selling Novel's\n")
Novels


# In[89]:


driver.close()


# Q7. Scrape the details most watched tv series of all time from imdb.com. 
# Url = https://www.imdb.com/list/ls095964455/
# You have to find the following details:
# A) Name
# B) Year span
# C) Genre
# D) Run time
# E) Ratings
# F) Votes

# In[90]:


# getting web driver
driver=webdriver.Chrome(r'C:\Users\Acer\Downloads\chromedriver_win32\chromedriver.exe')


# In[91]:


# getting the web page
url='https://www.imdb.com/list/ls095964455/'
driver.get(url)


# In[92]:


# finding the web element for all the required details and scrape them.
tv_name=[]
year_span=[]
tv_tag=driver.find_elements(By.XPATH, '//h3[@class="lister-item-header"]')
for i in tv_tag:
    tv_name.append((i.text).split('(')[0])
    year_span.append((i.text).split('(')[1])

len(tv_name),len(year_span)


# In[93]:


genr=[]
gen_tag=driver.find_elements(By.XPATH,'//p[@class="text-muted text-small"]/span[5]')
for i in gen_tag:
    genr.append(i.text)
len(genr)


# In[95]:


run_time=[]
run_tag=driver.find_elements(By.XPATH, '//p[@class="text-muted text-small"]/span[3]')
for i in run_tag:
    run_time.append(i.text)
len(run_time)


# In[96]:


rating=[]
rate_tag=driver.find_elements(By.XPATH,'//div[@class="ipl-rating-star small"]/span[2]')
for i in rate_tag:
    rating.append(i.text)
len(rating)


# In[97]:


votes=[]
temp=[]
vote_tag=driver.find_elements(By.XPATH,'//p[@class="text-muted text-small"]/span[2]')
for i in vote_tag:
    temp.append(i.text)
for i in range(1,len(temp),2):
    votes.append(temp[i])
len(votes)


# In[98]:


# preparing dataframe
Tv_Series=pd.DataFrame({'Series Name':tv_name, 'Year Span':year_span, 'Genre':genr,
                       'Run Time': run_time, 'Rating':rating, 'Votes': votes})
print("Top 100 most watched TV Series\n")
Tv_Series


# In[99]:


driver.close()


# 8. Details of Datasets from UCI machine learning repositories. 
# Url = https://archive.ics.uci.edu/
# You have to find the following details:
# A) Dataset name
# B) Data type
# C) Task
# D) Attribute type
# E) No of instances
# F) No of attribute
# G) Year
# Note: - from the home page you have to go to the ShowAllDataset page through code.

# In[100]:


# getting web driver
driver=webdriver.Chrome(r'C:\Users\Acer\Downloads\chromedriver_win32\chromedriver.exe')


# In[101]:


# getting the web page
url ='https://archive.ics.uci.edu/'
driver.get(url)


# In[102]:


# finding web element and clicking on view all tab.
view_all_tag=driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/span/b/a')
view_all_tag.click()


# In[103]:


# finding web element for all the required details and scrape them
dataset=[]
ds_name_tag=driver.find_elements(By.XPATH,'//p[@class="normal"]/b')
for i in ds_name_tag:
    dataset.append(i.text)
len(dataset)


# In[104]:


data_type=[]
type_tag=driver.find_elements(By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/p')
for i in type_tag[1:]:
    data_type.append(i.text)
len(data_type)


# In[105]:


task=[]
task_tag=driver.find_elements(By.XPATH,'/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[3]/p')
for i in task_tag[1:]:
    task.append(i.text)
len(task)


# In[106]:


attribute_type=[]
attri_tag=driver.find_elements(By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[4]/p')
for i in attri_tag[1:]:
    attribute_type.append(i.text)
len(attribute_type)


# In[107]:


instance=[]
instance_tag=driver.find_elements(By.XPATH,'/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[5]/p')
for i in instance_tag[1:]:
    instance.append(i.text)
len(instance)


# In[108]:


num_attribute=[]
num_attri_tag=driver.find_elements(By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[6]/p')
for i in num_attri_tag[1:]:
    num_attribute.append(i.text)
len(num_attribute)


# In[109]:


Year=[]
y_tag=driver.find_elements(By.XPATH,'/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[7]/p')
for i in y_tag[1:]:
    Year.append(i.text)
len(Year)


# In[110]:


# preparing dataframe
Datasets= pd.DataFrame({'Dataset Name':dataset,'Data Type': data_type, 'Task': task, 
                       'Attribute Type':attribute_type, 'Instances':instance, 
                        'Number Of Attribute': num_attribute, 'Year':Year})
print("List of all the Dataset Present in the site.")
Datasets


# In[ ]:




