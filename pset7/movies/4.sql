-- Write a SQL query to determine the number of movies with an IMDb rating of 10.0.
select count(rating) as "Number of movies with a 10.0 rating" from ratings where rating = 10.0;