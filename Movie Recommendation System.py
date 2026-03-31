try:
    import pandas as pd
except:
    print(" Pandas not installed. Installing now...")
    import os
    os.system("pip install pandas")
    import pandas as pd

try:
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except:
    print("Sklearn not installed. Installing now...")
    import os
    os.system("pip install scikit-learn")
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity


movies = [
    {"title": "Avatar", "tags": "action adventure sci-fi space alien"},
    {"title": "Titanic", "tags": "romance drama ship love tragedy"},
    {"title": "Avengers", "tags": "action superhero marvel fight world"},
    {"title": "Iron Man", "tags": "tech billionaire suit marvel action"},
    {"title": "Thor", "tags": "god hammer marvel fantasy action"},
    {"title": "Hulk", "tags": "monster anger science action"},
    {"title": "Batman Begins", "tags": "dark hero crime action dc"},
    {"title": "The Dark Knight", "tags": "joker crime thriller dc"},
    {"title": "Superman", "tags": "alien flying hero dc"},
    {"title": "Man of Steel", "tags": "alien hero dc action"},
    {"title": "Doctor Strange", "tags": "magic marvel time multiverse"},
    {"title": "Interstellar", "tags": "space science future emotional"},
    {"title": "Inception", "tags": "dream mind thriller sci-fi"},
    {"title": "Matrix", "tags": "virtual reality future action"},
    {"title": "John Wick", "tags": "revenge gun action thriller"},
    {"title": "Fast and Furious", "tags": "cars racing action family"},
    {"title": "Mission Impossible", "tags": "spy agent action thriller"},
    {"title": "Harry Potter", "tags": "magic wizard school fantasy"},
    {"title": "Joker", "tags": "dark villain psychology crime"},
    {"title": "Deadpool", "tags": "comedy antihero marvel action"},
    {"title": "Spider Man", "tags": "hero teenager marvel action"},
    {"title": "Black Panther", "tags": "king africa tech marvel"},
    {"title": "Captain America", "tags": "war hero marvel shield"},
    {"title": "Shutter Island", "tags": "mystery psychological thriller"},
    {"title": "Fight Club", "tags": "dark psychology underground"},
    {"title": "The Godfather", "tags": "mafia crime family drama"},
    {"title": "3 Idiots", "tags": "education friendship comedy india"},
    {"title": "Dangal", "tags": "sports wrestling india motivation"},
    {"title": "Bahubali", "tags": "epic war king india action"},
    {"title": "KGF", "tags": "gold mafia power action"},
    {"title": "Pushpa", "tags": "smuggling attitude action"},
    {"title": "RRR", "tags": "freedom action drama india"},
    {"title": "Drishyam", "tags": "crime suspense family thriller"},
    {"title": "War", "tags": "spy action india"},
    {"title": "Pathaan", "tags": "spy action bollywood"},
    {"title": "Jawan", "tags": "mass action bollywood"},
    {"title": "Animal", "tags": "dark intense action"},
]

df = pd.DataFrame(movies)

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['tags']).toarray()

similarity = cosine_similarity(vectors)

input("Please enter your name :")
def recommend(movie_name):
    movie_name = movie_name.strip()

    if movie_name not in df['title'].values:
        print("\n Movie not found! Try another one.\n")
        return

    index = df[df['title'] == movie_name].index[0]
    distances = similarity[index]

    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)

    print(f"\n Top Recommendations for '{movie_name}':\n")

    count = 0
    for i in movie_list[1:]:
        print("👉", df.iloc[i[0]].title)
        count += 1
        if count == 7:
            break

print(" Movie Recommendation System Ready!\n")

while True:
    user_input = input("Enter a movie name (or type 'exit'): ")

    if user_input.lower() == "exit":
        print("👋 Exiting... Bye!")
        break

    recommend(user_input)