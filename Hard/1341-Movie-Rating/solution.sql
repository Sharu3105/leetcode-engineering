(SELECT name AS results
 FROM Users u
 JOIN MovieRating mr ON u.user_id = mr.user_id
 GROUP BY u.user_id
 ORDER BY COUNT(*) DESC, name ASC
 LIMIT 1)
UNION ALL
(SELECT title AS results
 FROM Movies m
 JOIN MovieRating mr ON m.movie_id = mr.movie_id
 WHERE created_at LIKE '2020-02%'
 GROUP BY m.movie_id
 ORDER BY AVG(rating) DESC, title ASC
 LIMIT 1);
