# Do we still get those same sparks on-screen?

## Overview
A Python project that compares Nicholas Sparks' books with their film adaptations using data from the Google Books API and Rotten Tomatoes.

## How it works
- Google Books API: The program queries the Google Books API to fetch a list of Nicholas Sparks' books. For each book, it retrieves details like the title, published date, average rating, and the number of ratings.
- Rotten Tomatoes Web Scraping: The program scrapes Rotten Tomatoes for data on Nicholas Sparks' film adaptations. It gathers details such as the movie title, Tomatometer score, box office earnings, and release year.
- Comparison: The program then compares each book with its corresponding movie adaptation to observe differences in ratings, popularity, and release timelines.

## Setup
1. Clone the repo:
bash
Copy code
git clone https://github.com/yourusername/On-Screen-Sparks.git
cd On-Screen-Sparks
2. Create .env with your API key:
env
Copy code
GOOGLEBOOKS_API_KEY=your_api_key
3. Install dependencies:
bash
Copy code
pip install -r requirements.txt
4. Run the program:
bash
Copy code
python data_extraction.py
python main.py

## Files
- data_extraction.py: Outputs merged book and movie data as CSV file
- main.py: Preliminary data cleaning and Main analysis
- .env: Holds API key

## Limitations
- API Rate Limits: The Google Books API has a daily query limit, so be mindful of hitting rate limits when running the program multiple times in a day.
- Incomplete Data: Some books or movies may not have complete data available on Rotten Tomatoes or Google Books, which could affect comparisons.

## Future Improvements
Extend the comparison to include audience scores or other relevant metrics.

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome!
