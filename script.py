from source import WebSource
import pickle
import pandas as pd

def main():
    
    result = []
    pattern = 'https://www.kinopoisk.ru/index.php?level=6&view_best_box=1&view_best_box=3&view_year={}'
    for year in range(2008, 2018):
        url = pattern.format(str(year))
        links = WebSource(url).get_links()
        i = 0
        for link in links:
            info_movie = WebSource(link).get_info_about_movie(year)
            if info_movie:
                result.append(info_movie)
                i += 1
            if i == 20:
                break
    user_data_df = pd.DataFrame(result)
    user_data_df.to_csv('movies_list.csv', encoding = 'utf-8')

if __name__  == '__main__':
    main()
