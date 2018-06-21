from bs4 import BeautifulSoup
import requests
import re

#############
# FUNCTIONS #
#############

def get_list_of_NY_urls():
    url_list = []

    ny_url = 'https://fletchercareertrips.com/ny-career-trip/site-visits/'

    r = requests.get(ny_url)

    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.find_all('a', attrs={'href': re.compile('^https://fletchercareertrips.com/ny-career-trip/site-visits/')}):
        url_list.append(link.get('href'))

    return url_list

def get_list_of_DC_urls():
    url_list = []

    dc_url = 'https://fletchercareertrips.com/dc-career-trip/site-visits/'

    r = requests.get(dc_url)

    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.find_all('a', attrs={'href': re.compile('^https://fletchercareertrips.com/dc-career-trip/site-visits/')}):
        url_list.append(link.get('href'))

    return url_list


#############
# MAIN CODE #
#############

## Press F5 to run the code. HTML files will be saved wherever this python script is saved. 

NY_list = get_list_of_NY_urls()
DC_list = get_list_of_DC_urls()

## To write from the other career trip, just change the line below to use
## the other list. (i.e. if it says "for url in DC_list", change it to say
## "for url in NY_list"

for url in DC_list:
    try: 
        print("writing from url: " + url)
        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')
        page_title = soup.find('h1').get_text(strip=True)

        f = open(page_title + ".html", "w")
        f.write(str(soup))
        f.close()
        
    except:
        continue
