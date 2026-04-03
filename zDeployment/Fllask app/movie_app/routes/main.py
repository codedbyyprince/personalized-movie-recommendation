from movie_app.services.supabase_client import supabase 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Load embeddings from the Flask app package directory.
vectors_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'movie_embeddings.npy')
embd = np.load(vectors_path, allow_pickle=True)
embd = np.nan_to_num(embd, nan=0.0, posinf=0.0, neginf=0.0)
similarity_matrix = cosine_similarity(embd)


def get_movie_details(title):
    result = (
        supabase.table("tmdb_with_index")
        .select("*")
        .ilike("title", f"%{title}%")
        .execute()
    )
    return result.data[0] if result.data else None

def search_movie(query):
    try:
        # Use ilike for case-insensitive partial matching
        # This works better than text_search for queries with numbers and multiple words
        pattern = f"%{query}%"
        print(f"[DEBUG] Searching for movies with pattern: {pattern}")
        
        response = (
            supabase
            .table('tmdb_with_index')
            .select("*")
            .ilike("title", pattern)
            .limit(20)
            .execute()
        )
        
        print(f"[DEBUG] Search for '{query}' returned {len(response.data)} results")
        for movie in response.data:
            print(f"  - Found: {movie.get('title', 'N/A')}")
        
        return response.data if response.data else []
    except Exception as e:
        print(f"[ERROR] Search failed: {str(e)}")
        return []


def by_genre(genre):
    pattern = f"%{genre}%"
    result = (
        supabase.table("tmdb_with_index")
        .select("*")
        .ilike("genre_names", pattern)   # ✅ works because column is text
        .execute()
    )
    return result
    return result
def recommend_for_movie(movie, n=7):
    pattern = f"%{movie}%"
    found = (
        supabase.table("tmdb_with_index")
        .select("*")
        .ilike("title", pattern)
        .execute()
    )

    movie_id = int(found.data[0]['row_index'])

    score = similarity_matrix[movie_id]

    similar_indices = np.argsort(score)[::-1][1:n+1].tolist()

    similar_movies = (
        supabase.table("tmdb_with_index")
        .select("*")
        .in_("row_index", similar_indices)
        .execute()
    )

    return similar_movies.data
