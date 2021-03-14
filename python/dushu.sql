CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    href VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL,
    alphabet VARCHAR(1) NOT NULL,
    description MEDIUMTEXT,
    loaded BOOLEAN NOT NULL DEFAULT FALSE,
    download_ebook_count INT DEFAULT 0,
    download_pdf_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS chapters (
    chapter_id INT NOT NULL,
    book_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (book_id, chapter_id),
    FOREIGN KEY (book_id) REFERENCES books (id) ON UPDATE RESTRICT ON DELETE CASCADE
)  ENGINE=INNODB;

ALTER TABLE books CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE books DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE books CHANGE title title VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci;

ALTER TABLE chapters CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE chapters DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE chapters CHANGE title title VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE chapters CHANGE content content TEXT CHARACTER SET utf8 COLLATE utf8_general_ci;

-- ALTER TABLE chapters MODIFY content MEDIUMTEXT;

CREATE TABLE IF NOT EXISTS series (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    serie_id INT DEFAULT 0,
    serie_title VARCHAR(255) NOT NULL,
    href VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books (id) ON UPDATE RESTRICT ON DELETE CASCADE
)  ENGINE=INNODB;

ALTER TABLE series CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE series DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE series CHANGE serie_title serie_title VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci;

-- fix some missing columns
UPDATE books SET download_ebook_count = 0 and download_pdf_count = 0 
WHERE id not in (select book_id from chapters);

UPDATE books SET description = "无内容简介"
WHERE description is Null OR LENGTH(description) <= 1; 

UPDATE books SET author = "佚名" WHERE author = '';

-- book has series
SELECT s.book_id,b2.title, b1.id,s.serie_title
    FROM series as s LEFT JOIN books as b1  
    ON s.serie_title = b1.title 
    LEFT JOIN books as b2 ON s.book_id = b2.id ORDER BY s.book_id;

-- serie_id is foreign key to books id
UPDATE series
INNER JOIN books ON (series.serie_title = books.title)
SET series.serie_id = books.id;

CREATE TABLE IF NOT EXISTS search (
    id INT AUTO_INCREMENT PRIMARY KEY,
    query VARCHAR(50) NOT NULL,
    ip VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  ENGINE=INNODB;

ALTER TABLE search CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE search DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE search CHANGE query query VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci;