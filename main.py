import pandas as pd
import re

# Load the CSV data
data = pd.read_csv('nicholas_sparks_combined.csv')

#print(data['Movie_Tomatometer'].dtype)

# Transform the 'Movie_Tomatometer' column to float
data['Movie_Tomatometer'] = data['Movie_Tomatometer'].str.rstrip('%').astype(float)

# confirm that movie rating is a float data type
#print(data['Movie_Tomatometer'].dtype)

# # Preliminary data analysis
# print("Preliminary Data Analysis:")
# print("\nFirst few rows of the dataset:")
# print(data.head())

# print("\nMissing values in each column:")
# print(data.isnull().sum())

# print("\nData types of each column:")
# print(data.dtypes)

# print("\nUnique values in 'Movie_Tomatometer' column:")
# print(data['Movie_Tomatometer'].unique())

# print("\nUnique values in 'Movie_BoxOffice_Earnings' column:")
# print(data['Movie_BoxOffice_Earnings'].unique())


def calculate_performance(title):
    row = data[data['book_title'] == title].iloc[0]
    
    # Book performance calculation
    book_rating = row['book_average_rating'] if pd.notna(row['book_average_rating']) else 0
    book_score = book_rating * 20  # Convert 5-star rating to 100-point scale
    
    # Movie performance calculation
    movie_score = row['Movie_Tomatometer']  # Already a float, no need for conversion
    
    return book_score, movie_score


def compare_performance(title):
    book_score, movie_score = calculate_performance(title)
    row = data[data['book_title'] == title].iloc[0]
    
    print(f"\nPerformance comparison for {title}:")
    print(f"\nBook performance:")
    print(f"  - Average rating: {row['book_average_rating']} out of 5")
    print(f"  - Book score: {book_score:.2f}%")
    
    print(f"\nMovie performance:")
    print(f"  - Tomatometer rating: {row['Movie_Tomatometer']}%")
    print(f"  - Movie score: {movie_score:.2f}%")
    
    print("\nCalculation explanation:")
    print("Book score = Average rating * 20 (converts 5-star scale to 100-point scale)")
    print("Movie score = Tomatometer rating (already on a 100-point scale)")
    
    if book_score > movie_score:
        print(f"\nThe book performed better with a score of {book_score:.2f}% compared to the movie's score of {movie_score:.2f}%.")
    elif movie_score > book_score:
        print(f"\nThe movie performed better with a score of {movie_score:.2f}% compared to the book's score of {book_score:.2f}%.")
    else:
        print(f"\nThe book and movie performed equally with a score of {book_score:.2f}%.")


def print_instructions():
    print("\n" + "=" * 60)
    print("Nicholas Sparks Book vs. Movie Adaptation Comparator")
    print("=" * 60)
    print("This program compares the performance of Nicholas Sparks' books")
    print("and their movie adaptations using data from Google Books and Rotten Tomatoes.")
    print("=" * 60)

def print_menu():
    print("\nChoose a title:")
    print("1. The Notebook")
    print("2. Safe Haven")
    print("3. Message in a Bottle")
    print("4. Exit")

def main():
    while True:
        print_instructions()
        print_menu()
        
        choice = input("Enter the number of your choice (1-4): ")
        
        if choice == '4':
            print("Thank you for using the comparator. Goodbye!")
            break
        
        titles = ["The Notebook", "Safe Haven", "Message in a Bottle"]
        if choice in ['1', '2', '3']:
            selected_title = titles[int(choice) - 1]
            compare_performance(selected_title)
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()