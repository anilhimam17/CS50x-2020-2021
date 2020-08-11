-- Write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.
select name as "Directors of movies with ratings >= 9.0" from people
where id in (select person_id from directors where movie_id in (select movie_id from ratings where rating >= 9.0));