import pandas as pd
from bs4 import BeautifulSoup
import requests
# from google.colab import drive, files
# from google.colab import auth
# auth.authenticate_user()

# Mounting Google Drive
# drive.mount('/content/drive')

# Root website link
root = 'https://subslikescript.com'
website = f'{root}/movies/'

def multiple_movies_data(website):
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    
    # Extracting all movie links
    movie_title = box.find_all('a', href=True)
    movie_list = [movie_element['href'] for movie_element in movie_title]

    movies_data = []  # List to store multiple movies

    for movie_element in movie_list:
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

    return movies_data  # Return a list of movies

# Calling the function outside the loop
movies = multiple_movies_data(website)

# Saving multiple movies to separate text files
for title, transcript in movies:
    with open(f'{title}.txt', 'w', encoding="utf-8") as file:
        file.write(transcript)
    print(f"Saved: {title}.txt")
