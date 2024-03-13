-- a script that print full description of a table
-- from a database if it exists
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'your_table_name' AND TABLE_SCHEMA = 'your_database_name';
