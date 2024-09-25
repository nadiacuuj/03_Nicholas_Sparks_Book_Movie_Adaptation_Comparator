import pandas as pd
import re

# Load the CSV data
data = pd.read_csv('nicholas_sparks_combined.csv')

def calculate_performance(title):
    row = data[data['book_title'] == title].iloc[0]
    
    # Book performance
    book_score = row['book_average_rating'] * row['book_total_rating_count']
    
    # Movie performance
    movie_rating = float(re.sub(r'[^\d.]', '', row['Movie_Tomatometer'])) / 100
    movie_earnings = float(re.sub(r'[^\d.]', '', row['Movie_BoxOffice_Earnings']))
    movie_score = movie_rating * movie_earnings
    
    return book_score, movie_score

def compare_performance(title):
    book_score, movie_score = calculate_performance(title)
    row = data[data['book_title'] == title].iloc[0]
    
    print(f"\nPerformance comparison for {title}:")
    print(f"Book performance:")
    print(f"  - Average rating: {row['book_average_rating']}")
    print(f"  - Total ratings: {row['book_total_rating_count']}")
    print(f"  - Book score: {book_score:.2f}")
    
    print(f"\nMovie performance:")
    print(f"  - Tomatometer rating: {row['Movie_Tomatometer']}")
    print(f"  - Box office earnings: {row['Movie_BoxOffice_Earnings']}")
    print(f"  - Movie score: {movie_score:.2f}")
    
    if book_score > movie_score:
        print(f"\nThe book performed better with a score of {book_score:.2f} compared to the movie's score of {movie_score:.2f}.")
    elif movie_score > book_score:
        print(f"\nThe movie performed better with a score of {movie_score:.2f} compared to the book's score of {book_score:.2f}.")
    else:
        print(f"\nThe book and movie performed equally with a score of {book_score:.2f}.")

# Main program
print("Choose a title:")
print("1. The Notebook")
print("2. Safe Haven")
print("3. Message in a Bottle")

choice = input("Enter the number of your choice (1-3): ")

titles = ["The Notebook", "Safe Haven", "Message in a Bottle"]
if choice in ['1', '2', '3']:
    selected_title = titles[int(choice) - 1]
    compare_performance(selected_title)
else:
    print("Invalid choice. Please run the program again and select a number between 1 and 3.")