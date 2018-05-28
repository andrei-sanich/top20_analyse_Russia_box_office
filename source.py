from bs4 import BeautifulSoup
from selenium import webdriver
import time


class WebSource():
    
   
    def __init__(self, url):

        self.url = url
        self.driver = webdriver.PhantomJS()
        
    def get_links(self):

        self.driver.get(self.url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find('div', class_='block_left')
        movies = div.find_all('a')[6:-2]
        links = ["https://www.kinopoisk.ru" + movie.get('href') for movie in movies]
        return links
       
    
    def get_info_about_movie(self, year):

        self.driver.get(self.url)
        time.sleep(5)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        
        table = soup.find('table', {'class': 'info'})
        movie_year = int(table.find('td', {'class': 'type'}, text = u'год').nextSibling.nextSibling.text[:5])
        if movie_year == year:

            genres = [x.text for x in table.find('span', {'itemprop': 'genre'}).find_all('a')]
            countries = [x.text for x in table.find('td', {'class': 'type'}, text = u'страна').nextSibling.nextSibling.find_all('a')]
            duration = int(table.find('td', {'class': 'type'}, text = u'время').nextSibling.text.split()[0])
            
            info = {
                    'genres': genres,
                    'countries': countries,
                    'movie_duration': duration,
                    'year': movie_year
                        }
            return info    
        else:
            return False
