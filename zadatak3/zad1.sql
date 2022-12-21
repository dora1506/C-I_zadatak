ALTER TABLE public."playerInfo"
ADD COLUMN "ageCategory" text,
ADD COLUMN "goalsPerClubGame" float;

UPDATE public."playerInfo"
SET "ageCategory" = (CASE 
	WHEN age <= 23 THEN 'Young'
	WHEN age >= 33 THEN 'Old'
	ELSE 'MidAge'
END),
"goalsPerClubGame" = (CASE
	WHEN "numOfAppsClub" > 0 THEN "numOfGoalsClub"/"numOfAppsClub"::float
	ELSE 0::float
END);