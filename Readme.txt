============================================================
Required packages
============================================================
IMDbPY
Installation instructions: http://imdbpy.sourceforge.net/docs/README.txt
OR: pip install IMDbPY


============================================================
To build the LM training data (run in console)
============================================================
python LM_training_data.py


============================================================
To test the genres of synopses (run in console)
============================================================
Recommended (faster): python genre_search.py -b small_LM_build.data -t test.input -o output.txt
Not recommended (slower): python genre_search.py -b large_LM_build.data -t test.input -o output.txt


============================================================
Provided test.input and output.txt from running recommended test
============================================================
Test environment:
- Movie titles and genres from IMDB
- Word bigram
- Training data size of only 3464 movie entries


Pacific Rim
Genres: Action | Adventure | Sci-Fi
Result: Horror: 50.0%, Sci-Fi: 16.6666666667%, War: 16.6666666667%, History: 16.6666666667%
Src: http://www.imdb.com/title/tt1663662/

Mulan
Genres: Animation | Adventure | Family | Fantasy | Musical | War
Result: Animation: 96.2264150943%, Western: 1.88679245283%, Musical: 1.88679245283%
Src: http://www.imdb.com/title/tt0120762/

Inception
Genres: Action | Mystery | Sci-Fi | Thriller
Result: Crime: 18.75%, War: 12.5%, Film-Noir: 12.5%, Western: 12.5%, Animation: 6.25%, Music: 6.25%, Horror: 6.25%, Adventure: 6.25%, Thriller: 6.25%, Mystery: 6.25%, Fantasy: 6.25%
Src: http://www.imdb.com/title/tt1375666/

Shutter Island
Genres: Mystery | Thriller
Result: Action: 28.5714285714%, Sci-Fi: 14.2857142857%, Comedy: 14.2857142857%, Horror: 14.2857142857%, Western: 14.2857142857%, Mystery: 14.2857142857%
Src: http://www.imdb.com/title/tt1130884/

The Rock
Genres: Action | Adventure | Thriller
Result: Crime: 13.1578947368%, Action: 13.1578947368%, Sci-Fi: 10.5263157895%, Film-Noir: 10.5263157895%, Mystery: 10.5263157895%, History: 7.89473684211%, Romance: 5.26315789474%, Animation: 5.26315789474%, Horror: 5.26315789474%
Src: http://www.imdb.com/title/tt0117500/

Con Air
Genres: Action | Crime | Thriller
Result: Action: 85.1351351351%, War: 4.05405405405%, Sci-Fi: 2.7027027027%, Crime: 1.35135135135%, Animation: 1.35135135135%, Film-Noir: 1.35135135135%, Western: 1.35135135135%, Sport: 1.35135135135%, Biography: 1.35135135135%
Src: http://www.imdb.com/title/tt0118880/

The Terminator
Genres: Action | Sci-Fi
Result: Sci-Fi: 91.4285714286%, War: 2.85714285714%, Horror: 2.85714285714%, Action: 2.85714285714%
Src: http://www.imdb.com/title/tt0088247/

Frozen
Genres: Animation | Adventure | Comedy | Family | Fantasy | Musical
Result: Animation: 25.0%, Musical: 25.0%, Crime: 12.5%, Romance: 12.5%, Music: 12.5%, Drama: 12.5%
Src: http://www.imdb.com/title/tt2294629/

RoboCop
Genres: Action | Crime | Sci-Fi | Thriller
Result: Sci-Fi: 88.3720930233%, Crime: 2.32558139535%, Animation: 2.32558139535%, Music: 2.32558139535%, Western: 2.32558139535%, Action: 2.32558139535%
Src: http://www.imdb.com/title/tt0093870/

Suits
Genres: Comedy | Drama
Result: Crime: 25.0%, Comedy: 12.5%, War: 12.5%, Film-Noir: 12.5%, Adventure: 12.5%, Action: 12.5%, Musical: 12.5%
Src: http://www.imdb.com/title/tt1632701/


============================================================
Things that could be improved
============================================================
- In the output, genres with 0% could be removed
- A larger sized training data could aid in accuracy
- Include more information from other forms of popular media, like books and television series


============================================================
Personal thoughts
============================================================

IMDB was chosen as it provides a friendly interface to retrieve data about thousands of movie from.
It also helps that sticking with a single source improves consistency in informational quality as well.

Getting data from IMDB is time consuming, because spamming IMDB's servers with connections is a sureway to get them upset.
Generating large_LM_build.data took over 6 hours, which is only around 15% of the available movie IDs from the larger CSV file (which would probably take around 40 hours).
Also, generating the LM each time a test is run was also quite time consuming, as the program had to go through all these genres and synopses that were retrieved from IMDB.
All in all, testing this was a lot more time consuming than I had expected, and I should have started on this sooner. 

Attempting to use a trigram or 4-gram resulted in too many misses to make any significant judgment, due to the limited size of the training data.
Hence, I settled with word bigrams which were more accurate than word unigrams and most character-based n-gram models (based on tests).

On another note, while a synopsis is an alright estimator for a movie's genre, I do not think that it is an terribly accurate way to judge any given movie's genre. 
In order to avoid being spoiling potential viewers, synopses may not include plot twists or major plot points that could greatly affect its genre.
A synopsis merely conveys a rough outline of a movie's plot points, and a genre is not made up of solely plot points.
Other factors that synopses fail to capture is how a movie is executed, its tone, and other cinematographic techniques that can cause its genre to vary.


============================================================
Legal matters
============================================================

Information courtesy of
IMDb
(http://www.imdb.com).
Used with permission.