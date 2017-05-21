-- Questions: 
-- https://lagunita.stanford.edu/courses/Engineering/db/2014_1/courseware/ch-sql/seq-exercise-sql_movie_query_core-pastdue/

-- Q1
SELECT title FROM Movie WHERE director = 'Steven Spielberg';

-- Q2
SELECT DISTINCT Movie.year
FROM Movie 
INNER JOIN Rating On Movie.mID = Rating.mID
WHERE Rating.stars = 4 OR Rating.stars = 5
ORDER BY Movie.year ASC;

-- Solution:
select distinct year
from Movie, Rating
where Rating.mID = Movie.mID and stars >= 4
order by YEar;

-- Q3
SELECT Movie.title
FROM Movie
LEFT JOIN Rating On Movie.mID = Rating.mID
WHERE Rating.stars IS NULL;

-- Solution:
select title
from Movie
where mID not in (select mID 
                  from Rating)
;

-- Q4
SELECT DISTINCT Reviewer.name
FROM Reviewer
INNER JOIN Rating ON Reviewer.rID = Rating.rID
WHERE Rating.ratingDate IS NULL;

-- Solution:
select distinct name
from Reviewer, Rating
where Reviewer.rID = Rating.rID and ratingDate is NULL;

-- Q5
SELECT Reviewer.name, Movie.title, Rating.stars, Rating.ratingDate
FROM Rating
INNER JOIN Reviewer ON Reviewer.rID = Rating.rID
INNER JOIN Movie ON Movie.mID = Rating.mID
ORDER BY Reviewer.name, Movie.title, Rating.stars ASC;

-- Solution:
select name, title, stars, ratingDate
from Movie, Rating, Reviewer
where Movie.mID = Rating.mID and Reviewer.rID = Rating.rID
order by name, title, stars;

-- Q6
-- For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, return the reviewer's name and the title of the movie. 

-- SELECT A.rID, A.mID
-- FROM Rating A, Rating B
-- WHERE A.rID = B.rID AND A.mID = B.mID AND A.ratingDate < B.ratingDate AND A.stars < B.stars

SELECT Reviewer.name, Movie.title
FROM Rating A, Rating B
INNER JOIN Reviewer ON Reviewer.rID = A.rID
INNER JOIN Movie ON Movie.mID = A.mID
WHERE A.rID = B.rID AND A.mID = B.mID AND A.ratingDate < B.ratingDate AND A.stars < B.stars

-- Solution:
select name, title
from Movie, Reviewer, (select R1.rID, R1.mID
  from Rating R1, Rating R2
  where R1.rID = R2.rID 
  and R1.mID = R2.mID
  and R1.stars < R2.stars
  and R1.ratingDate < R2.ratingDate) C
where Movie.mID = C.mID
and Reviewer.rID = C.rID;
