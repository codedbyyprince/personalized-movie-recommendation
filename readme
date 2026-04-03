# Personalized Movie Picks

A movie recommendation web application built with Flask. It shows movies organized by genre on the homepage, lets users click into any movie to see details and similar recommendations, and supports search by title. The recommendation engine uses cosine similarity on feature embeddings built from movie metadata.

Built by **Prince Nagda**.

---

## How It Works

The homepage loads movies grouped by genre, similar to how streaming platforms present content. When a user clicks on a movie, the app fetches its details from the database and runs the recommendation engine to find the most similar movies. Search works by partial title matching across the full dataset.

The recommendation logic uses a precomputed cosine similarity matrix built from movie embeddings. At request time, the app looks up the selected movie's index, retrieves its similarity scores against all other movies, and returns the top results.

---

## Recommendation Approach

**v1, KNN based (exploration)** used K-Nearest Neighbors on movie features to find similar titles. This was the starting point to understand the problem and validate the data pipeline.

**v2, Embedding + Cosine Similarity (final)** generates dense feature vectors for each movie using a combination of genre, overview text, and keywords. These embeddings are stored as a NumPy file and loaded at startup. Cosine similarity is computed across all embeddings at load time, producing a similarity matrix that is used directly for recommendations. This approach is faster at request time and captures semantic similarity better than KNN on raw features.

---

## Data

6,000+ movies sourced from the TMDB API. Each movie record includes title, overview, genres, keywords, poster URL, release date, and runtime. Movie data is stored in a Supabase database and queried live at request time.

---

## Pages

**Home** shows movies organized into genre rows, Action, Comedy, Family, Animation, Romance, Thriller, Horror, and Science Fiction. Each row displays movie posters that link to the detail page.

**Movie detail** shows the selected movie's poster, title, release date, runtime, overview, and genres. Below the details, a recommendations section shows similar movies based on the cosine similarity engine.

**Search** accepts a title query and returns matching movies using case-insensitive partial matching. Results are shown as a poster grid with titles.

---

## Project Structure

```
Train_v1/              KNN based exploration notebooks
Train_v2/              Embedding generation, feature scaling, final training notebooks
zDeployment/
  Flask app/
    movie_app/
      routes/
        main.py        Recommendation logic, similarity matrix, Supabase queries
      services/
        movie_services.py     Movie listing service
        supabase_client.py    Supabase connection setup
      __init__.py      Flask app factory, route definitions
    movie_embeddings.npy   Precomputed embedding vectors
    app.py             Entry point
```

---

## Tech Stack

Python, Flask, scikit-learn, NumPy, Supabase, TMDB API, Render.

---

## Author

Prince Nagda

