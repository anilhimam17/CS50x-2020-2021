-- Write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year.
select name "Actors in movies of 2004" from people
where id in (select person_id from stars where movie_id in (select id from movies where year = 2004))
order by birth;