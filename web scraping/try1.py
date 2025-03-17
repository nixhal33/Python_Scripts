from bs4 import BeautifulSoup
import requests
import os

# Website URL
root_web = 'https://www.empireonline.com'
sec_web = f'{root_web}/movies/features/best-movies-2/'

def movies_title_scrape(sec_web):
    result = requests.get(sec_web)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Find all movie containers
    movies = soup.find_all('span', class_='content_content__i0P3p')

    if not movies:
        print("No movies found. Check the class name or website structure.")
        return []

    print(f"Found {len(movies)} movies.")

    movie_data = []

    for movie in movies:  # Looping through each movie span
        try:
            # Extract Title
            title_tag = movie.find('h2')
            if title_tag:
                strong_tag = title_tag.find('strong')
                title = strong_tag.get_text(strip=True) if strong_tag else "No Title Found"
            else:
                title = "No Title Found"

            # Store movie details
            movie_text = f"Title: {title}\n{'-'*50}\n"
            movie_data.append(movie_text)

        except Exception as e:
            print(f"Error Processing movie: {e}")
    
    return movie_data

# Scrape movies
movies_list = movies_title_scrape(sec_web)

# Save to text files
target_directory = '/home/nix/Documents/py_scripts/Python_Scripts/web scraping/scraped_movies'
os.makedirs(target_directory, exist_ok=True)

for idx, movie_text in enumerate(movies_list):
    file_path = os.path.join(target_directory, f"movie_{idx+1}.txt")
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(movie_text)
    print(f"Saved: {file_path}")