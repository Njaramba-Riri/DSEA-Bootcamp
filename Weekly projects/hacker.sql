SELECT name FROM Hackers ha
INNER JOIN Submissions su ON ha.hacker_id=su.hacker_id
SELECT name FROM ha Hackers;

SELECT submission_date, COUNT(DISTINCT hacker_id) AS unique_hackers,
    MIN(hacker_id) AS hacker_id, hacker_name
FROM submissions su
GROUP BY submission_date, hacker_name
HAVING COUNT(submission_id) >= 1
ORDER BY submission_date ASC, COUNT(DISTINCT hacker_id) DESC, hacker_id ASC;