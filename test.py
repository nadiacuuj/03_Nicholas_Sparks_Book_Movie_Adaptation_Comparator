# import pandas as pd

# # Load the CSV data
# data = pd.read_csv('nicholas_sparks_combined.csv')

# # Transform 'Movie_Tomatometer' to float
# data['Movie_Tomatometer'] = data['Movie_Tomatometer'].str.rstrip('%').astype(float)

# # Convert 'Movie_BoxOffice_Earnings' to numeric
# def convert_box_office(value):
#     if isinstance(value, str) and 'M' in value:
#         return float(value.replace('M', '').replace('$', '').replace(',', '')) * 1_000_000
#     return float(value.replace('$', '').replace(',', ''))

# data['Movie_BoxOffice_Earnings'] = data['Movie_BoxOffice_Earnings'].apply(convert_box_office)

# def calculate_performance(title):
#     row = data[data['book_title'] == title].iloc[0]
    
#     # Book performance
#     book_rating = row['book_average_rating'] if pd.notna(row['book_average_rating']) else 0
#     book_ratings_count = row.get('book_ratings_count', 0)
    
#     # Movie performance
#     movie_rating = row['Movie_Tomatometer']
#     movie_box_office = row['Movie_BoxOffice_Earnings']
    
#     # Min and max for normalization
#     min_ratings_count = data['book_ratings_count'].min()
#     max_ratings_count = data['book_ratings_count'].max()
#     min_box_office = data['Movie_BoxOffice_Earnings'].min()
#     max_box_office = data['Movie_BoxOffice_Earnings'].max()
    
#     print(f"Book ratings count range: {min_ratings_count:,} to {max_ratings_count:,}")
#     print(f"Movie box office range: ${min_box_office:,.2f} to ${max_box_office:,.2f}")
    
#     # Calculate weights based on popularity
#     book_weight = book_ratings_count / max_ratings_count
#     movie_weight = movie_box_office / max_box_office
    
#     # Calculate weighted scores
#     book_score = (book_rating * 20) * (1 + book_weight)
#     movie_score = movie_rating * (1 + movie_weight)
    
#     return book_score, movie_score, book_rating, movie_rating, book_ratings_count, movie_box_office

# def compare_performance(title):
#     book_score, movie_score, book_rating, movie_rating, book_ratings_count, movie_box_office = calculate_performance(title)
    
#     print(f"\nPerformance comparison for {title}:")
#     print(f"\nBook performance:")
#     print(f"  - Average rating: {book_rating} out of 5")
#     print(f"  - Total ratings: {book_ratings_count:,}")
#     print(f"  - Book score: {book_score:.2f}%")
    
#     print(f"\nMovie performance:")
#     print(f"  - Tomatometer rating: {movie_rating}%")
#     print(f"  - Box office earnings: ${movie_box_office:,.2f}")
#     print(f"  - Movie score: {movie_score:.2f}%")
    
#     print("\nCalculation explanation:")
#     print("Book score = (Average rating * 20) * (1 + Book ratings count weight)")
#     print("Movie score = Tomatometer rating * (1 + Box office earnings weight)")
    
#     # Explain the weight calculation
#     print("\nWeight Calculation Explanation:")
#     print("The weight is calculated by dividing the current value by the maximum value.")
#     print("This normalizes the value between 0 and 1, enhancing scores based on popularity.")
    
#     if book_score > movie_score:
#         print(f"\nThe book performed better with a score of {book_score:.2f}% compared to the movie's score of {movie_score:.2f}%.")
#     elif movie_score > book_score:
#         print(f"\nThe movie performed better with a score of {movie_score:.2f}% compared to the book's score of {book_score:.2f}%.")
#     else:
#         print(f"\nThe book and movie performed equally with a score of {book_score:.2f}%.")

# def print_instructions():
#     print("\n" + "=" * 60)
#     print("Nicholas Sparks Book vs. Movie Performance Comparator")
#     print("=" * 60)
#     print("This program compares the performance of Nicholas Sparks' books")
#     print("and their movie adaptations using data from Goodreads and Rotten Tomatoes.")
#     print("=" * 60)

# def print_menu():
#     print("\nChoose a title:")
#     print("1. The Notebook")
#     print("2. Safe Haven")
#     print("3. Message in a Bottle")
#     print("4. Exit")

# def main():
#     while True:
#         print_instructions()
#         print_menu()
        
#         choice = input("Enter the number of your choice (1-4): ")
        
#         if choice == '4':
#             print("Thank you for using the comparator. Goodbye!")
#             break
        
#         titles = ["The Notebook", "Safe Haven", "Message in a Bottle"]
#         if choice in ['1', '2', '3']:
#             selected_title = titles[int(choice) - 1]
#             compare_performance(selected_title)
#             input("\nPress Enter to continue...")
#         else:
#             print("Invalid choice. Please select a number between 1 and 4.")
#             input("\nPress Enter to continue...")

# if __name__ == "__main__":
#     main()