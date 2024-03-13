-- Get the ID of the genre "Comedy"
SELECT id FROM tv_genres WHERE name = 'Comedy';

-- Use the genre ID to select all shows not linked to the genre
SELECT tv_shows.title 
FROM tv_shows 
WHERE id NOT IN (
    SELECT show_id 
    FROM tv_show_genres 
    WHERE genre_id = [Comedy's ID]
) 
ORDER BY title;
