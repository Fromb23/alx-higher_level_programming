-- Get the ID of the show "Dexter"
SELECT id FROM tv_shows WHERE title = 'Dexter';

-- Use the show ID to select all genres not linked to the show
SELECT tv_genres.name 
FROM tv_genres 
WHERE id NOT IN (
    SELECT genre_id 
    FROM tv_show_genres 
    WHERE show_id = [Dexter's ID]
) 
ORDER BY name;
