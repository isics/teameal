# Ceux qui mangent le plus
SELECT auth_user.username, COUNT(app_meal.id) meals
FROM auth_user
JOIN app_meal ON (app_meal.user_id = auth_user.id)
GROUP BY auth_user.id
ORDER BY meals DESC, auth_user.username;


# Ceux qui cuisinent le plus dans l'absolu
SELECT auth_user.username, COUNT(app_meal.id) cooks
FROM auth_user
JOIN app_meal ON (app_meal.user_id = auth_user.id)
WHERE app_meal.cook=1
GROUP BY auth_user.id
ORDER BY cooks DESC, auth_user.username;


# Ceux qui cuisinent le plus relativement au nombre de repas
SELECT auth_user.username, COUNT(app_meal.id) meals, ROUND(SUM(app_meal.cook)/COUNT(app_meal.id)*100,1) cooks
FROM auth_user
JOIN app_meal ON (app_meal.user_id = auth_user.id)
GROUP BY auth_user.id
ORDER BY cooks DESC, auth_user.username;


# Ceux qui nettoyent le plus relativement au nombre de repas
SELECT auth_user.username, COUNT(app_meal.id) meals, ROUND(SUM(app_meal.maid)/COUNT(app_meal.id)*100,1) maids
FROM auth_user
JOIN app_meal ON (app_meal.user_id = auth_user.id)
GROUP BY auth_user.id
ORDER BY maids DESC, auth_user.username;