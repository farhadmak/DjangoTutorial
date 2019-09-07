CREATE TABLE tree (
    id integer PRIMARY KEY,
    neighbourhood_name text,
    location_type text,
    species_botanical text,
    species_common text,
    genus text,
    species text,
    cultivar text,
    diameter_breast_height int,
    condition_percent int,
    planted_date date,
    owner text,
    bears_edible_fruit text,
    type_of_edible_fruit text,
    count int,
    latitude real,
    longitude real,
    location text

);

-- example data entry
-- 517802,
-- Callaghan,
-- Boulevard,
-- Ulmus americana,
-- "Elm, American",
-- Ulmus,
-- americana,
-- Brandon,
-- 12,
-- 70,
-- 2014-06-01,
-- Parks,
-- No,
-- N/A,
-- 1,
-- 53.40397946501458,
-- -113.53568383736352,
-- "(53.40397946501458, -113.53568383736352)"


.mode csv
.import Trees.csv tree
