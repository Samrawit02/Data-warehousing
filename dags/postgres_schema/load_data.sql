-- LOAD DATA LOCAL INFILE '/usr/local/airflow/dags/data.csv'
-- INTO TABLE trafic_data
-- FIELDS TERMINATED BY ';'
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

COPY trafic_data FROM '/dags/data.csv' DELIMITER ',' CSV HEADER
