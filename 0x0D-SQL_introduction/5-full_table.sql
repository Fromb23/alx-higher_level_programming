-- a script that print full description of a table
-- from a database if it exists
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = first_table AND TABLE_SCHEMA = mysql
