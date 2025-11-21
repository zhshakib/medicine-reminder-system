CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

-- Using Simple Medicine Table 
-- So that it will be easy to `CRUD` the medicines
-- Not Recommended for large scale projects

CREATE TABLE IF NOT EXISTS medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    dosage TEXT,
    times TEXT, 
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
