DROP TABLE IF EXISTS blogs;
CREATE TABLE blogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    image TEXT,
    description TEXT NOT NULL,
    author TEXT NOT NULL
);