def movie_organizer(*movie_tuples_in_tuple):
    movie_dict = {}
    for movie_tuple in movie_tuples_in_tuple:
        movie_name = movie_tuple[0]
        movie_genre = movie_tuple[1]
        if movie_genre not in movie_dict.keys():
            movie_dict[movie_genre] = [movie_name]
        else:
            movie_dict[movie_genre].append(movie_name)
    sorted_movie_dict = dict(sorted(movie_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    output_list = []
    for movie_genre, movie_names_list in sorted_movie_dict.items():
        count_genre_movies = len(movie_names_list)
        genre_info = f"{movie_genre} - {count_genre_movies}"
        output_list.append(genre_info)
        sorted_movie_names_list = sorted(movie_names_list)
        for movie_name in sorted_movie_names_list:
            name_info = f"* {movie_name}"
            output_list.append(name_info)
    output = "\n".join(output_list)
    return output


# print(movie_organizer(
#     ("The Matrix", "Sci-fi")))


# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))


# print(movie_organizer(
#     ("Avatar: The Way of Water", "Action"),
#     ("House Of Gucci", "Drama"),
#     ("Top Gun", "Action"),
#     ("Ted", "Comedy"),
#     ("Duck Soup", "Comedy"),
#     ("The Dark Knight", "Action"),
#     ("A Star Is Born", "Musicals"),
#     ("The Warrior", "Action"),
#     ("Like A Boss", "Comedy"),
#     ("The Green Mile", "Drama"),
#     ("21 Jump Street", "Comedy")))
