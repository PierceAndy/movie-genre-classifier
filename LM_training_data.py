from csv import DictReader
import imdb


def main():
	imdb_movie_IDs = get_list_of_imdb_movie_IDs()
	extract_genres_synopsis(imdb_movie_IDs)


def get_list_of_imdb_movie_IDs():
	"""Gets lits of IMDB movie IDs to use with IMDB's online DB.
	Src: http://grouplens.org/datasets/movielens/"""

	csv_filepath = "data/links.csv"

	with open(csv_filepath) as csv_file:
		imdb_movie_IDs = [row["imdbId"] for row in DictReader(csv_file)]

	return imdb_movie_IDs


def extract_genres_synopsis(imdb_movie_IDs):
	"""Extracts genres and the plot synopsis based on movie ID from IMDB"""

	with open("data/LM_build.data", "w") as output_file, \
			open("debug/debug.txt", "w", 0) as debug_file:

		for ID in imdb_movie_IDs:
			try:
				debug_file.write("Adding " + str(ID) + "...\n")

				imdb_access = imdb.IMDb()
				movie = imdb_access.get_movie(ID)
				genres = movie["genres"]
				plot = movie["plot"][0] # Several variations exist, get first plot summary

				# Format: "Action/Drama/Comedy <synopsis text>"
				output_file.write("/".join(genres) + " " + plot + "\n")

			except Exception as error:
				debug_file.write("Error: " + str(ID) + ", Reason: " + str(error) + "\n")


if __name__ == "__main__":
	main()
