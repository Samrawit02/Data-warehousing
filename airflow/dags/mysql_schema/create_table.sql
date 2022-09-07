CREATE TABLE IF NOT EXISTS trafic_data
(   id serial,
    track_id integer,
    type text,
    traveled_d numeric,
    avg_speed numeric,
    lat numeric,
    lon numeric,
    speed numeric,
    lon_acc numeric,
    lat_acc numeric,
    time numeric
);