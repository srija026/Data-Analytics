CREATE TABLE IF NOT EXISTS dim_date (
    date_id INT IDENTITY(1,1) PRIMARY KEY,
    date DATE NOT NULL,
    day INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_location (
    location_id INT IDENTITY(1,1) PRIMARY KEY,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS fact_uber_rides (
    ride_id INT IDENTITY(1,1) PRIMARY KEY,
    date_id INT,
    location_id INT,
    cost DECIMAL(10, 2),
    distance DECIMAL(10, 2),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id)
);

CREATE TABLE IF NOT EXISTS fact_uber_eats (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    date_id INT,
    location_id INT,
    cost DECIMAL(10, 2),
    restaurant VARCHAR(100),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id)
);
