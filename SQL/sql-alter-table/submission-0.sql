CREATE TABLE books (
  id INTEGER,
  title TEXT,
  author TEXT
);
-- Do not modify above this line --

ALter table books ADD COLUMN published_year INTEGER;
Alter Table books RENAME COlumn id to isbn;
alter table books DROP Column author;









-- Do not modify below this line --
SELECT column_name, data_type, column_default
FROM information_schema.columns
WHERE table_name = 'books'
ORDER BY column_name;
