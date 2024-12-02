import time
import requests
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv('TMDBAPIKEY')
TMDBAPIReadAccessToken = os.getenv('TMDBAPIReadAccessToken')

BASE_URL = "https://api.themoviedb.org/3"

url = "https://api.themoviedb.org/3/search/movie"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDBAPIReadAccessToken}"
}



def fetch_release_date(movie_title, on_streaming_date=None):
    """
    Fetch release date of a movie using TMDb API and ensure it is before the on_streaming_date.
    """
    params = {
        "query": movie_title,
        "api_key": API_KEY,
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                # Get the release dates of all relevant results
                for result in data["results"]:
                    release_date = result.get("release_date", None)
                    if release_date:
                        # Ensure release_date is a string
                        if isinstance(release_date, pd.Timestamp) or isinstance(release_date, datetime):
                            release_date_str = release_date.strftime("%Y-%m-%d")
                        else:
                            release_date_str = str(release_date)
                        
                        # Convert release_date_str to datetime object
                        release_date_obj = datetime.strptime(release_date_str, "%Y-%m-%d")
                        
                        # If no streaming date is provided, ensure the release year <= 2024
                        if not on_streaming_date:
                            if release_date_obj.year <= 2024:
                                return release_date_str
                        else:
                            # on_streaming_date is already a datetime object
                            if release_date_obj < on_streaming_date and release_date_obj.year <= 2024:
                                return release_date_str
                return None  # No valid release date found
            else:
                return None  # No results found
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"Exception occurred for movie '{movie_title}': {e}")
        return None



# Search and update release dates for missing date
def update_release_dates(movies_df):
    """Update missing in_theaters_date for movies."""
    
    missing_movies = movies_df[movies_df['in_theaters_date'].isna()]
    # Create a dictionary to store results
    release_dates = {}

    for index, row in missing_movies.iterrows():
        title = row['movie_title']
        on_streaming_date = row.get('on_streaming_date', None)
        release_dates[title] = fetch_release_date(title, on_streaming_date)
        time.sleep(0.25)

    # Update DataFrame with fetched release dates
    for title, release_date in release_dates.items():
        movies_df.loc[movies_df['movie_title'] == title, 'in_theaters_date'] = release_date


    return movies_df



# Map missing content rating

def get_movie_id_by_title(title):
    """
    Fetch the TMDb movie ID using the movie title.
    :param title: Movie title
    :return: Movie ID or error message
    """
    params = {"api_key": API_KEY, "query": title}
    response = requests.get(url, headers = headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            return data["results"][0]["id"]
        else:
            return None  # Movie not found
    else:
        return None  # Error fetching movie ID
    
def get_content_rating(movie_id, region="US"):
    """
    Fetch the content rating (e.g., PG, R) of a movie.
    :param movie_id: TMDb movie ID
    :param region: Region for content rating (default is 'US')
    :return: Content rating or 'Not Rated'
    """
    url_releasedate = f"{BASE_URL}/movie/{movie_id}/release_dates"
    params = {"api_key": API_KEY}
    response = requests.get(url_releasedate, params=params)
    
    if response.status_code == 200:
        data = response.json()
        ratings = data.get("results", [])
        for rating in ratings:
            if rating["iso_3166_1"] == region:
                # Iterate over release_dates to find the first valid certification
                for release_date in rating["release_dates"]:
                    certification = release_date.get("certification", "")
                    if certification:  # Return the first valid certification found
                        return certification
        return "Not Rated"  
    else:
        return f"Error: {response.status_code}"  

def get_movie_content_rating_by_title(title, region="US"):
    """
    Fetch content rating by movie title.
    :param title: Movie title
    :param region: Region for content rating (default is 'US')
    :return: Content rating or error message
    """
    movie_id = get_movie_id_by_title(title)
    if isinstance(movie_id, int):
        return get_content_rating(movie_id, region)
    else:
        return movie_id
    
# Process all missing titles
def fetch_missing_ratings(titles, region="US"):
    """
    Fetch ratings for a list of titles.
    :param titles: List of movie titles
    :param region: Region for content rating
    :return: Dictionary with titles and ratings
    """
    ratings = {}
    for title in titles:
        print(f"Fetching rating for: {title}")
        rating = get_movie_content_rating_by_title(title, region)
        ratings[title] = rating
        time.sleep(0.3)  # Rate limiting to avoid API ban
    return ratings