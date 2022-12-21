SELECT name,(
SELECT COUNT(*)
FROM public."playerInfo" as t1
WHERE t1.age < t2.age 
AND t1.position = t2.position
AND t1."numOfAppsNational" > t2."numOfAppsNational")
FROM public."playerInfo" as t2
WHERE "currentClub" = 'Liverpool'