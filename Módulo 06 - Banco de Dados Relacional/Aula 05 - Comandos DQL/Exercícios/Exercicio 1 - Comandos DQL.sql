-- A)
SELECT title, author FROM books;

-- B)
SELECT * FROM books WHERE author = 'Henry Davis';

-- C)
SELECT title, author, release_year FROM books WHERE release_year < 1900;

-- D)
SELECT * FROM books WHERE title LIKE 'O%';

-- E)
SELECT title, author FROM books WHERE release_year > 1950;

-- F)
SELECT COUNT(*) FROM books;

-- G)
SELECT author "Autor", COUNT(*) quantidade FROM books
GROUP BY author
ORDER BY quantidade DESC
LIMIT 1;

-- H)
SELECT * FROM books
ORDER BY release_year;

-- I)
SELECT title FROM books
ORDER BY release_year
LIMIT 1;

-- J)
SELECT title FROM books
ORDER BY release_year
LIMIT 1;

-- K)
SELECT title, author FROM books
ORDER BY id DESC
LIMIT 3;