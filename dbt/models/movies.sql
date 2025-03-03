SELECT  CAST(id as INT) as movie_id, 
    TO_DATE("Release_Date", 'YY-MM-DD') as release_date,
    "IMDB_URL" as imdb_url,
    CAST(CAST("Film_Noir" as INT) as BOOLEAN) as film_noir,
    CAST(CAST("Action" as INT) as BOOLEAN) as action,
    CAST(CAST("Adventure" as INT) as BOOLEAN) as adventure,
    CAST(CAST("Horror" as INT) as BOOLEAN) as horror,
    CAST(CAST("War" as INT) as BOOLEAN) as war,
    CAST(CAST("Romance" as INT) as BOOLEAN) as romance, 
    CAST(CAST("Western" as INT) as BOOLEAN) as western,
    CAST(CAST("Documentary" as INT) as BOOLEAN) as documentary,
    CAST(CAST("Sci_Fi" as INT) as BOOLEAN) as sci_fi,
    CAST(CAST("Drama" as INT) as BOOLEAN) as drama,
    CAST(CAST("Thriller" as INT) as BOOLEAN) as thriller,
    CAST(CAST("Crime" as INT) as BOOLEAN) as crime,
    CAST(CAST("Children_s" as INT) as BOOLEAN) as childrens,
    CAST(CAST("Fantasy" as INT) as BOOLEAN) as fantasy,
    CAST(CAST("Animation" as INT) as BOOLEAN) as animation,
    CAST(CAST("Comedy" as INT) as BOOLEAN) as comedy,
    CAST(CAST("Mystery" as INT) as BOOLEAN) as mystery, 
    CAST(CAST("Musical" as INT) as BOOLEAN) as musical
FROM {{ source('recommmender_system_raw', 'movies') }}




