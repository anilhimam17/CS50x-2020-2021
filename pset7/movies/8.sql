-- Write a SQL query to list the names of all people who starred in Toy Story.
select name as "Actors Starring in Toy Story" from people
where id in (select person_id from stars where movie_id = (select id from movies where title = "Toy Story"));