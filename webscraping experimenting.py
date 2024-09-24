# import required libraries
import os
from dotenv import load_dotenv

import requests
from bs4 import BeautifulSoup
import pandas as pd

# GOOGLEBOOKS_API_KEY is already defined in the .env file
# To retrieve, first, run "pip install python-dotenv" in terminal
# Then, load environment variables from .env file
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
            'title': book_info.get('title', 'N/A'),
            'published_date': book_info.get('publishedDate', 'N/A'),
            'average_rating': book_info.get('averageRating', 'N/A'),
            'ratings_count': book_info.get('ratingsCount', 'N/A')
        }
    return None # if book not found

# Usage example:
# 1. Get all Nicholas Sparks book titles
# all_books = get_nicholas_sparks_books()

# 2. Get details for each book
# for book_title in all_books:
#    book_details = get_book_details(book_title)
#    print(book_details)



# def scrape_rotten_tomatoes():
#     ROTTENTOMATOES_URL = "https://www.rottentomatoes.com/celebrity/nicholas-sparks"
#     response = requests.get(ROTTENTOMATOES_URL)
#     soup = BeautifulSoup(response.content, 'html.parser')
   
#     # Find all <td> elements with the class "celebrity-filmography__title"
#     title_cells = soup.find_all('td', class_='celebrity-filmography__title')
#     # Extract the text from the <a> elements within each <td>
#     titles = [cell.find('a').text.strip() for cell in title_cells if cell.find('a')]

#     # Find all <span> elements with the class "icon__tomatometer-score"
#     tomatometer_spans = soup.find_all('span', class_='icon__tomatometer-score')
#     # Extract the text from each tomatometer span
#     tomatometer_scores = [span.text.strip() for span in tomatometer_spans]

#     movie_data = []
#     for title, score in zip(titles, tomatometer_scores):
#         movie_data.append({
#             'Title': title,
#             'Tomatometer': score
#         })
    
#     return movie_data

# movies = scrape_rotten_tomatoes()
# for movie in movies:
#     print(f"Title: {movie['Title']}, Tomatometer: {movie['Tomatometer']}")


# def scrape_rotten_tomatoes():
#     ROTTENTOMATOES_URL = "https://www.rottentomatoes.com/celebrity/nicholas-sparks" # URL of Nicholas Sparks' Rotten Tomatoes page
#     response = requests.get(ROTTENTOMATOES_URL) # Send a GET request to the URL
#     soup = BeautifulSoup(response.content, 'html.parser') # Parse the HTML content of the page
   
#     # Find all <td> elements with the class "celebrity-filmography__title"
#     title_cells = soup.find_all('td', class_='celebrity-filmography__title')
#     # Extract the text from the <a> elements within each <td>
#     titles = [cell.find('a').text.strip() for cell in title_cells if cell.find('a')] # This creates a list of movie titles

#     # Find all <span> elements with the class "icon__tomatometer-score"
#     tomatometer_spans = soup.find_all('span', class_='icon__tomatometer-score')
#     tomatometer_scores = [span.text.strip() for span in tomatometer_spans]

#     # Find all <rt-text> elements with context_="label" for audience scores
#     audience_score_elements = soup.find_all('rt-text', context_='label')
#     audience_scores = [element.text.strip() for element in audience_score_elements]

#     movie_data = []
#     # Use zip() to iterate over titles, tomatometer_scores, and audience_scores simultaneously
#     for title, tomatometer, audience in zip(titles, tomatometer_scores, audience_scores):
#         movie_data.append({
#             'Title': title,
#             'Tomatometer': tomatometer,
#             'Audience Score': audience
#         })
    
#     return movie_data

# # Call the function to scrape the data
# movies = scrape_rotten_tomatoes()
# # Print each movie's title, Tomatometer score, and Audience Score
# for movie in movies:
#     print(f"Title: {movie['Title']}, Tomatometer: {movie['Tomatometer']}, Audience Score: {movie['Audience Score']}")



# def scrape_rotten_tomatoes():
#     ROTTENTOMATOES_URL = "https://www.rottentomatoes.com/celebrity/nicholas-sparks" # URL of Nicholas Sparks' Rotten Tomatoes page
#     response = requests.get(ROTTENTOMATOES_URL) # Send a GET request to the URL
#     soup = BeautifulSoup(response.content, 'html.parser') # Parse the HTML content of the page
   
#     # Find all <td> elements with the class "celebrity-filmography__title"
#     title_cells = soup.find_all('td', class_='celebrity-filmography__title')
#     # Extract the text from the <a> elements within each <td>
#     titles = [cell.find('a').text.strip() for cell in title_cells if cell.find('a')] # This creates a list of movie titles

#     # Find all <span> elements with the class "icon__tomatometer-score"
#     tomatometer_spans = soup.find_all('span', class_='icon__tomatometer-score')
#     tomatometer_scores = [span.text.strip() for span in tomatometer_spans]

#     # Find all <rt-text> elements with context="label" for audience scores
#     audience_score_elements = soup.find_all('rt-text', context='label')
#     audience_scores = [element.text.strip() for element in audience_score_elements]

#     movie_data = []
#     # Use zip() to iterate over titles, tomatometer_scores, and audience_scores simultaneously
#     for title, tomatometer, audience in zip(titles, tomatometer_scores, audience_scores):
#         movie_data.append({
#             'Title': title,
#             'Tomatometer': tomatometer,
#             'Audience Score': audience
#         })
    
#     return movie_data

# # Call the function to scrape the data
# movies = scrape_rotten_tomatoes()
# # Print each movie's title and Tomatometer score
# for movie in movies:
#     print(f"Title: {movie['Title']}, Tomatometer: {movie['Tomatometer']}, Audience Score: {movie['Audience Score']}")


# def scrape_rotten_tomatoes():
#     ROTTENTOMATOES_URL = "https://www.rottentomatoes.com/celebrity/nicholas-sparks" # URL of Nicholas Sparks' Rotten Tomatoes page
#     response = requests.get(ROTTENTOMATOES_URL) # Send a GET request to the URL
#     soup = BeautifulSoup(response.content, 'html.parser') # Parse the HTML content of the page
   
#     # Find all <td> elements with the class "celebrity-filmography__title"
#     title_cells = soup.find_all('td', class_='celebrity-filmography__title')
#     # Extract the text from the <a> elements within each <td>
#     titles = [cell.find('a').text.strip() for cell in title_cells if cell.find('a')] # This creates a list of movie titles

#     # Find all <span> elements with the class "icon__tomatometer-score"
#     tomatometer_spans = soup.find_all('span', class_='icon__tomatometer-score')
#     tomatometer_scores = [span.text.strip() for span in tomatometer_spans]

#     # Find all <rt-text> elements with context="label" for audience scores
#     audience_score_elements = soup.find_all('rt-text', context='label')
#     audience_scores = [element.text.strip() for element in audience_score_elements]

#     # Find all <td> elements with the class "celebrity-filmography__box-office"
#     box_office_cells = soup.find_all('td', class_='celebrity-filmography__box-office')
#     box_office_data = [cell.text.strip() for cell in box_office_cells]

#     movie_data = []
#     # Use zip() to iterate over titles, tomatometer_scores, audience_scores, and box_office_data simultaneously
#     for title, tomatometer, audience, box_office in zip(titles, tomatometer_scores, audience_scores, box_office_data):
#         movie_data.append({
#             'Title': title,
#             'Tomatometer': tomatometer,
#             'Audience Score': audience,
#             'Box Office': box_office
#         })
    
#     return movie_data

# # Call the function to scrape the data
# movies = scrape_rotten_tomatoes()
# # Print each movie's title, Tomatometer score, Audience Score, and Box Office
# for movie in movies:
#     print(f"Title: {movie['Title']}, Tomatometer: {movie['Tomatometer']}, Audience Score: {movie['Audience Score']}, Box Office: {movie['Box Office']}")


# # WORKING VERSION
# def scrape_rotten_tomatoes():
#     ROTTENTOMATOES_URL = "https://www.rottentomatoes.com/celebrity/nicholas-sparks" # URL of Nicholas Sparks' Rotten Tomatoes page
#     response = requests.get(ROTTENTOMATOES_URL) # Send a GET request to the URL
#     soup = BeautifulSoup(response.content, 'html.parser') # Parse the HTML content of the page
   
#     # Find all <td> elements with the class "celebrity-filmography__title"
#     title_cells = soup.find_all('td', class_='celebrity-filmography__title')
#     # Extract the text from the <a> elements within each <td>
#     titles = [cell.find('a').text.strip() for cell in title_cells if cell.find('a')] # This creates a list of movie titles

#     # Find all <span> elements with the class "icon__tomatometer-score"
#     tomatometer_spans = soup.find_all('span', class_='icon__tomatometer-score')
#     tomatometer_scores = [span.text.strip() for span in tomatometer_spans]

#     # Find all <rt-text> elements with context="label" for audience scores
#     audience_score_elements = soup.find_all('rt-text', context='label')
#     audience_scores = [element.text.strip() for element in audience_score_elements]

#     # Find all <td> elements with the class "celebrity-filmography__box-office"
#     box_office_cells = soup.find_all('td', class_='celebrity-filmography__box-office')
#     box_office_data = [cell.text.strip() for cell in box_office_cells]

#     # Find all <td> elements with the class "celebrity-filmography__year"
#     year_cells = soup.find_all('td', class_='celebrity-filmography__year')
#     years = [cell.text.strip() for cell in year_cells]

#     movie_data = []
#     # Use zip() to iterate over titles, tomatometer_scores, audience_scores, box_office_data, and years simultaneously
#     for title, tomatometer, audience, box_office, year in zip(titles, tomatometer_scores, audience_scores, box_office_data, years):
#         movie_data.append({
#             'Title': title,
#             'Tomatometer': tomatometer,
#             'Audience Score': audience,
#             'Box Office': box_office,
#             'Year': year
#         })
    
#     return movie_data

# # Call the function to scrape the data
# movies = scrape_rotten_tomatoes()
# # Print each movie's title, Tomatometer score, Audience Score, Box Office, and Year
# for movie in movies:
#     print(f"Title: {movie['Title']}, Tomatometer: {movie['Tomatometer']}, Audience Score: {movie['Audience Score']}, Box Office: {movie['Box Office']}, Year: {movie['Year']}")




# # MOST UP TO DATE WORKING VERSION
# def scrape_rotten_tomatoes():
#     ROTTENTOMATOES_URL = "https://www.rottentomatoes.com/celebrity/nicholas-sparks" # URL of Nicholas Sparks' Rotten Tomatoes page
#     response = requests.get(ROTTENTOMATOES_URL) # Send a GET request to the URL
#     soup = BeautifulSoup(response.content, 'html.parser') # Parse the HTML content of the page
   
#     # Find all <td> elements with the class "celebrity-filmography__title"
#     title_cells = soup.find_all('td', class_='celebrity-filmography__title')
#     # Extract the text from the <a> elements within each <td>
#     titles = [cell.find('a').text.strip() for cell in title_cells if cell.find('a')] # This creates a list of movie titles

#     # Find all <span> elements with the class "icon__tomatometer-score"
#     tomatometer_spans = soup.find_all('span', class_='icon__tomatometer-score')
#     tomatometer_scores = [span.text.strip() for span in tomatometer_spans]

#     # Find all <rt-text> elements with context="label" for audience scores
#     audience_score_elements = soup.find_all('rt-text', attrs={'context': 'label'})
#     audience_scores = [element.text.strip() for element in audience_score_elements]

#     # Find all <td> elements with the class "celebrity-filmography__box-office"
#     box_office_cells = soup.find_all('td', class_='celebrity-filmography__box-office')
#     box_office_data = [cell.text.strip() for cell in box_office_cells]

#     # Find all <td> elements with the class "celebrity-filmography__year"
#     year_cells = soup.find_all('td', class_='celebrity-filmography__year')
#     years = [cell.text.strip() for cell in year_cells]

#     movie_data = []
#     # Use zip() to iterate over titles, tomatometer_scores, audience_scores, box_office_data, and years simultaneously
#     for title, tomatometer, audience, box_office, year in zip(titles, tomatometer_scores, audience_scores, box_office_data, years):
#         movie_data.append({
#             'Title': title,
#             'Tomatometer': tomatometer,
#             'Audience Score': audience,
#             'Box Office': box_office,
#             'Year': year
#         })
    
#     return movie_data

# # Call the function to scrape the data
# movies = scrape_rotten_tomatoes()
# # Print each movie's title, Tomatometer score, Audience Score, Box Office, and Year
# for movie in movies:
#     print(f"Title: {movie['Title']}, Tomatometer: {movie['Tomatometer']}, Audience Score: {movie['Audience Score']}, Box Office: {movie['Box Office']}, Year: {movie['Year']}")


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

    # # Find all <rt-text> elements with context="label" for audience scores
    # audience_score_elements = soup.find_all('rt-text', attrs={'context': 'label'})
    # audience_scores = [element.text.strip() for element in audience_score_elements]

    # Find all <td> elements with the class "celebrity-filmography__box-office"
    box_office_cells = soup.find_all('td', class_='celebrity-filmography__box-office')
    box_office_data = [cell.text.strip() for cell in box_office_cells]

    # Find all <td> elements with the class "celebrity-filmography__year"
    year_cells = soup.find_all('td', class_='celebrity-filmography__year')
    years = [cell.text.strip() for cell in year_cells]

    movie_data = []
    # Use zip() to iterate over titles, tomatometer_scores, box_office_data, and years simultaneously
    for title, tomatometer, box_office, year in zip(titles, tomatometer_scores, box_office_data, years):
    #for title, tomatometer, audience, box_office, year in zip(titles, tomatometer_scores, box_office_data, years):
        movie_data.append({
            'Title': title,
            'Tomatometer': tomatometer,
            #'Audience Score': audience,
            'Box Office': box_office,
            'Year': year
        })
    
    return movie_data

# Call the function to scrape the data
movies = scrape_rotten_tomatoes()
# Print each movie's title, Tomatometer score, Audience Score, Box Office, and Year
for movie in movies:
    print(f"Title: {movie['Title']}, Tomatometer: {movie['Tomatometer']}, Box Office: {movie['Box Office']}, Year: {movie['Year']}")
    #print(f"Title: {movie['Title']}, Tomatometer: {movie['Tomatometer']}, Audience: {movie['Audience']}, Box Office: {movie['Box Office']}, Year: {movie['Year']}")





# # trying smth out
# def scrape_rotten_tomatoes():
#     ROTTENTOMATOES_URL = "https://www.rottentomatoes.com/celebrity/nicholas-sparks"
#     response = requests.get(ROTTENTOMATOES_URL)
#     soup = BeautifulSoup(response.content, 'html.parser')
   
#     # Find all <td> elements with the class "celebrity-filmography__title"
#     title_cells = soup.find_all('td', class_='celebrity-filmography__title')
#     titles = [cell.find('a').text.strip() for cell in title_cells if cell.find('a')]

#     # Find all <span> elements with the class "icon__tomatometer-score"
#     tomatometer_spans = soup.find_all('span', class_='icon__tomatometer-score')
#     tomatometer_scores = [span.text.strip() for span in tomatometer_spans]

#     # Find all <rt-text> elements with context="label" for audience scores
#     audience_score_elements = soup.find_all('rt-text', attrs={'context': 'label'})
#     audience_scores = [element.text.strip() for element in audience_score_elements]

#     # Find all <td> elements with the class "celebrity-filmography__box-office"
#     box_office_cells = soup.find_all('td', class_='celebrity-filmography__box-office')
#     box_office_data = [cell.text.strip() for cell in box_office_cells]

#     # Find all <td> elements with the class "celebrity-filmography__year"
#     year_cells = soup.find_all('td', class_='celebrity-filmography__year')
#     years = [cell.text.strip() for cell in year_cells]

#     movie_data = []
#     for title, tomatometer, audience, box_office, year in zip(titles, tomatometer_scores, audience_scores, box_office_data, years):
#         movie_data.append({
#             'Title': title,
#             'Tomatometer': tomatometer,
#             'Audience Score': audience,
#             'Box Office': box_office,
#             'Year': year
#         })
    
#     return movie_data

# # Call the function to scrape the data
# movies = scrape_rotten_tomatoes()
# # Print each movie's title, Tomatometer score, Audience Score, Box Office, and Year
# for movie in movies:
#     print(f"Title: {movie['Title']}, Tomatometer: {movie['Tomatometer']}, Audience Score: {movie['Audience Score']}, Box Office: {movie['Box Office']}, Year: {movie['Year']}")