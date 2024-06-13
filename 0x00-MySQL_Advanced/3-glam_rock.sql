-- A SQL script that lists all bands with Glam rock as their main style,
-- ranked by their longevity.
-- Column names will be: band_name and lifespan (in years until 2022 - 
-- I'm only permited to use 2022 instead of YEAR(CURDATE())
-- I shoud use attributes formed and split for computing the lifespan.
-- My script can be executed on any database.
SELECT
    band_name,
    -- Using ternary operator.
    (IF(split IS NULL, 2022, split) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
