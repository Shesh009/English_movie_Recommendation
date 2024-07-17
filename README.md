# Movie Recommendation System

## Overview

This project implements a movie recommendation system using content-based filtering. It analyzes movie data from the TMDB dataset, including genres, cast, crew, keywords, and overviews, to suggest similar movies based on cosine similarity.

## Features

- **Movie Selection:** Allows users to select a movie from a dropdown list.
- **Recommendations:** Recommends top 5 similar movies based on the selected movie's attributes.
- **Interactive Interface:** Provides a button interface for easy navigation through recommendations.

## Technologies Used

- Python
- Pandas
- NumPy
- scikit-learn (sklearn)
- Streamlit

## Dataset

The system uses the TMDB 5000 Movie Dataset, consisting of detailed movie information including genres, cast, crew, keywords, and overviews.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install dependencies:**
   Ensure you have Python 3.x installed. Install required packages:
   ```bash
   pip install pandas numpy scikit-learn streamlit
   ```

3. **Download dataset:**
   Download `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` from Kaggle and place them in the project directory.

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```
   This command starts the Streamlit app. Open the provided URL in your browser to interact with the movie recommendation system.

## Usage

- Select a movie from the dropdown list.
- The system will display top 5 movie recommendations based on cosine similarity with the selected movie.

## Deployment

The project is deployed using [Render](https://movie-recommendation-hwn5.onrender.com/). You can access the deployed application at the provided URL.

## Example

![Screenshot](![Screenshot 2024-07-17 104758](https://github.com/user-attachments/assets/1bbdaf53-d566-4fb3-a4a4-7fdc5ca6767a))


## Credits

- **Data Source:** TMDB 5000 Movie Dataset from Kaggle

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
