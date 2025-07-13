
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    phone VARCHAR(15) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS forms (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT
);

INSERT INTO users (phone, password) VALUES
('7760873976', 'to_share@123'),
('9999999999', 'pass123');

INSERT INTO forms (title, description) VALUES
('KYC Form', 'Know Your Customer details collection form'),
('Feedback Form', 'Customer feedback survey form');
