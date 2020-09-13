#--------------------------------- 
# import modules
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import re

#---------------------------------
#     
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#---------------------------------
# get links from url    
def get_links(driver, sleep_time):

    # open driver window
    #driver.set_window_size(1024, 600)
    #driver.maximize_window()
    driver.get("https://www.youtube.com/watch?v=_f6IqFMIJNo&list=PLtfRFndo6b7J3oqqu_P5LTvR6glE7q5v6")    
            
    # wait some seconds
    time.sleep(sleep_time)
            
    # get information from url
    soup = bs(driver.page_source,'html.parser')
    res = soup.find_all('ytd-playlist-panel-video-renderer')  
            
    # check if there is information
    if len(res) > 0:
        main_url = 'https://www.youtube.com/watch?v='
        urls = re.findall('watch.*list', str(res))
        links = [main_url + str(a[8:-9]) for a in urls[::2]]
    # if there is no information return false
    else:
        links = False    
    return links

#---------------------------------
# set sleep timer
sleep_time = 2
# call function to get links
links = get_links(driver, sleep_time)
#counter = 0
for i in links:
	#counter+=1
	print(i)
	#print(counter)
	