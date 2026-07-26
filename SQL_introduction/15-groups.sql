-- Comment
SELECT score, COUNT(*) AS number
  GROUP BY score
  ORDER BY number DESC;

