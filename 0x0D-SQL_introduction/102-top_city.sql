--Displays the 3 cities with the highes average between July and August

SELECT city, AVG(temperatures.value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
