from bs4 import BeautifulSoup
import requests
import os

root_web = 'https://www.empireonline.com'
sec_web = f'{root_web}/movies/features/best-movies-2/'

def movies_title_scrape(sec_web):
    result = requests.get(sec_web)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    
    # FIX: Use find_all() to get multiple movies
    movies = soup.find('article', class_='article_content__HfTvf')
    
    movie_data = []
    
    for movie in movies:
        try:
            title = movie.find('h2').find('strong').text.strip() if movie.find('h2') else "No Title Found"
            director = movie.find_all('p')[0].text.strip() if len(movie.find_all('p')) > 0 else "No Director Found"
            starring = movie.find_all('p')[1].text.strip() if len(movie.find_all('p')) > 1 else "No Cast Found"
            description = movie.find_all('p')[2].text.strip() if len(movie.find_all('p')) > 2 else "No Description Found"

            movie_text = f"Title: {title}\nDirector: {director}\nStarring: {starring}\nDescription: {description}\n{'-'*50}\n"
            
            movie_data.append(movie_text)
        
        except Exception as e:
            print(f"Error Processing movie: {e}")
    
    return movie_data

movies_list = movies_title_scrape(sec_web)

# FIX: Ensure directory exists
target_directory = '/home/nix/Documents/py_scripts/Python_Scripts/web scraping/scraped_movies'
os.makedirs(target_directory, exist_ok=True)

# FIX: Save each movie properly without unpacking issues
for idx, movie_text in enumerate(movies_list):
    file_path = os.path.join(target_directory, f"movie_{idx+1}.txt")
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(movie_text)
    print(f"Saved: {file_path}")