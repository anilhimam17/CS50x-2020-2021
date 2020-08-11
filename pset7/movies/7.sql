-- Write a SQL query to list all movies released in 2010 and their ratings, in descending order by rating.
select movies.title, ratings.rating from movies join ratings on movies.id = ratings.movie_id where year = 2010
and rating is not null group by title order by rating desc;