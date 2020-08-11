-- Write a SQL query to list the titles and release years of all Harry Potter movies, in chronological order.
select title as "Title of the Movie", year as "Release Year"
from movies where title like "Harry Potter%" order by year asc;