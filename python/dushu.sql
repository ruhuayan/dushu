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
    serie_title VARCHAR(255) NOT NULL,
    href VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books (id) ON UPDATE RESTRICT ON DELETE CASCADE
)  ENGINE=INNODB;

ALTER TABLE series CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE series DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE series CHANGE serie_title serie_title VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci;

update books
set download_ebook_count = 0 and download_pdf_count = 0 
where id not in (select book_id from chapters);