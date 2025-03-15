import requests
from bs4 import BeautifulSoup
import os

root = 'https://subslikescript.com/'
website = f'{root}/movies_letter-G/'

def movies_to_scrape_G(website):
    # initializing for requests, parsing parser and beautifulsoup
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content,'lxml')
    box = soup.find('article', class_='main-article')

    # now extracting all the movie links
    movie_title = box.find_all('a',href=True) # this will find all the movie title inside anchor tag with it's link
    movies_list =  [movie_element['href'] for movie_element in movie_title]

    movies_data = [] # to store later on scraped movie list

    for movie_element in movies_list:
        movie_url = f'{root}/{movie_element}'
        result = requests.get(movie_url)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        box = soup.find('article', class_='main-article')

        if box:
            title = box.find('h1').get_text(strip=True) if box.find('h1') else "No Title Found"
            transcript_div = box.find('div', id='cue-app')
            transcript = transcript_div.get_text("\n") if transcript_div else "No Transcript Found"

            movies_data.append((title, transcript))  # Storing movie details

    return movies_data

# calling the function movies_to_scrape_G
movies = movies_to_scrape_G(website)

# directing the location where to store the scraped movie
target_directory = '/home/nix/Documents/py_scripts/Python_Scripts/web scraping/scraped_movies'
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# saving the movies 
for title, transcript in movies:
    file_path = os.path.join(target_directory, f'{title}.txt')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(transcript)
    print(f"Saved: {title}.txt")

print(f"All the Scraped data has been Saved!!! to {target_directory}")
