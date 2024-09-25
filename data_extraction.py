# import required libraries
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import pandas as pd

# In terminal run:
# pip install python-dotenv
# pip install -r requirements.txt

# GOOGLEBOOKS_API_KEY is already defined in the .env file
# To retrieve, first load environment variables from .env file
load_dotenv()
# Now, we can get the API key
GOOGLEBOOKS_API_KEY = os.getenv('GOOGLEBOOKS_API_KEY')

# Check if the API key is loaded
if GOOGLEBOOKS_API_KEY is None:
    raise ValueError("GOOGLEBOOKS_API_KEY is not set in the environment variables")
else:
    print("Google Books API key loaded successfully!")

GOOGLEBOOKS_URL = "https://www.googleapis.com/books/v1/volumes"

# Function to retrieve a list of Nicholas Sparks' book titles
def get_nicholas_sparks_books():
    # Set up parameters for API request
    params = {
        'q': 'inauthor:"Nicholas Sparks"',
        'key': GOOGLEBOOKS_API_KEY,
        'maxResults': 40  # Nicholas Sparks has authored "at least" 23 books, so I chose this upper bound just to be safe
    }
    # Send a GET request to the Google Books API
    response = requests.get(GOOGLEBOOKS_URL, params=params)
    # Extract the 'items' (books) from the JSON response
    books = response.json().get('items', [])
    # Return a list of book titles, filtering out any items without a title
    return [book['volumeInfo']['title'] for book in books if 'title' in book['volumeInfo']]

# Function to retrieve detailed information about a specific Nicholas Sparks book
def get_book_details(title):
    params = {
        'q': f'intitle:"{title}" inauthor:"Nicholas Sparks"',
        'key': GOOGLEBOOKS_API_KEY
    }
    response = requests.get(GOOGLEBOOKS_URL, params=params)
    books = response.json().get('items', [])
    # Extract and return book details if found
    if books:
        book_info = books[0]['volumeInfo']
        return {
            # chose to use lower case naming convention for book attributes (for differenciation from movie attributes)
            'book_title': book_info.get('title', 'N/A'),
            'book_published_date': book_info.get('publishedDate', 'N/A'),
            'book_average_rating': book_info.get('averageRating', 'N/A'),
            'book_total_rating_count': book_info.get('ratingsCount', 'N/A')
        }
    return None # if book not found

# Function to normalize book and movie titles to same format for comparison
def normalize_title(title):
    normalized = title.lower().strip()
    normalized = normalized.split('(')[0].strip()  # Remove anything in parentheses
    return normalized

# # Usage example:
# # 1. Get all Nicholas Sparks book titles
# all_books = get_nicholas_sparks_books()

# # 2. Get details for each book
# for book_title in all_books:
#    book_details = get_book_details(book_title)
#    print(book_details)


# without audience ratings (problem with <rt>)
def scrape_rotten_tomatoes():
    ROTTENTOMATOES_URL = "https://www.rottentomatoes.com/celebrity/nicholas-sparks" # URL of Nicholas Sparks' Rotten Tomatoes page
    response = requests.get(ROTTENTOMATOES_URL) # Send a GET request to the URL
    soup = BeautifulSoup(response.content, 'html.parser') # Parse the HTML content of the page
   
    # Find all <td> elements with the class "celebrity-filmography__title"
    title_cells = soup.find_all('td', class_='celebrity-filmography__title')
    # Extract the text from the <a> elements within each <td>
    titles = [cell.find('a').text.strip() for cell in title_cells if cell.find('a')] # This creates a list of movie titles

    # Find all <span> elements with the class "icon__tomatometer-score"
    tomatometer_spans = soup.find_all('span', class_='icon__tomatometer-score')
    tomatometer_scores = [span.text.strip() for span in tomatometer_spans]

    # Find all <td> elements with the class "celebrity-filmography__box-office"
    box_office_cells = soup.find_all('td', class_='celebrity-filmography__box-office')
    box_office_data = [cell.text.strip() for cell in box_office_cells]

    # Find all <td> elements with the class "celebrity-filmography__year"
    year_cells = soup.find_all('td', class_='celebrity-filmography__year')
    years = [cell.text.strip() for cell in year_cells]

    movie_data = []
    # Use zip() to iterate over titles, tomatometer_scores, box_office_data, and years simultaneously
    for title, tomatometer, box_office, year in zip(titles, tomatometer_scores, box_office_data, years):
        movie_data.append({
            # chose to use upper case naming convention for movie attributes
            'Movie_Title': title,
            'Movie_Tomatometer': tomatometer,
            'Movie_BoxOffice_Earnings': box_office,
            'Movie_ReleaseYear': year
        })
    
    return movie_data

# # Usage example: Call the function to scrape the data
# movies = scrape_rotten_tomatoes()
# # Print each movie's title, Tomatometer score, Audience Score, Box Office, and Year
# for movie in movies:
#     print(f"Movie_Title: {movie['Movie_Title']}, Movie_Tomatometer: {movie['Movie_Tomatometer']}, Movie_BoxOffice_Earnings: {movie['Movie_BoxOffice_Earnings']}, Movie_ReleaseYear: {movie['Movie_ReleaseYear']}")


# Fetch and merge data
all_books = get_nicholas_sparks_books()
book_data = [get_book_details(title) for title in all_books if get_book_details(title)]
movie_data = scrape_rotten_tomatoes()

# Merge datasets based on Title
combined_data = []
for book in book_data:
    if book and 'book_title' in book:
        normalized_book_title = normalize_title(book['book_title'])
        for movie in movie_data:
            if 'Movie_Title' in movie:
                normalized_movie_title = normalize_title(movie['Movie_Title'])
                if normalized_book_title == normalized_movie_title:
                    combined_entry = {**book, **movie}
                    combined_data.append(combined_entry)

# # Convert to DataFrame and save to CSV
# df_combined = pd.DataFrame(combined_data)
# df_combined.to_csv('nicholas_sparks_combined.csv', index=False)

# print("Combined data saved to nicholas_sparks_combined.csv")