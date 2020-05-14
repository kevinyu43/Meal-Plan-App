# Meal-Plan-App
App that allows users to create meal plans.

## Get all food
### GET http://34.86.75.208/api/foods/
reponse: 
```json
{
	"success": true,
	"data": [
		{
			"id": 1,
			"name": "sausage",
			"difficulty": 6,
			"calories": 260
		}
	]
}
```
## Create a food 
### POST http://34.86.75.208/api/foods/
#### Sidenote: the difficulty must be between 0 and 10 or else there will be a 404 error
request body:
```json
{
	"name": "name",
	"calories": 999,
	"difficulty": 1
}
``` 
reponse: 
```json
{
	"success": true,
	"data": {
		"id": 1,
		"name": "sausage",
		"difficulty": 6,
		"calories": 260
	}
}
```
## Get a user by ID
### GET http://34.86.75.208/api/users/{id}/
response:
```json
{
	"success": true,
	"data": {
		"id": 1,
		"username": "kevin12",
		"meal_plans": [SERIALIZEDMEAL PLANS]
	}
}
```
## Create User
### POST http://34.86.75.208/api/users/
request body:
```json
{
	"username": "name"
}
```
response:
```json
{
	"success": true,
	"data": {
		"id": 1,
		"username": "kevin12",
		"meal_plans": [SERIALIZEDMEAL PLANS]
	}
}
```
## Delete User
### DELETE http://34.86.75.208/api/users/{id}/
response:
```json
{
	"success": true,
	"data": {
		"id": 1,
		"username": "kevin12",
		"meal_plans": [SERIALIZEDMEAL PLANS]
	}
}
```
## Get all meal plans
### GET http://34.86.75.208/api/meal_plans/
#### sidenote: the difficulty of the meal is the average difficulty of all the foods
response:
```json
{
	"success": true,
	"data": [
		{
			"id": 1,
			"name": "breakfast",
			"author_id": 4,
			"foods": [SERIALIZED FOODS],
			"total_calories": 100,
			"difficulty": 7.7
		},
		{
			"id": 2,
			"name": "lunch",
			"author_id": 3,
			"foods": [SERIALIZED FOODS],
			"total_calories": 999,
			"difficulty": 4.4
		}
	]
}
```
## Create meal plan
### POST http://34.86.75.208/api/meal_plans/
request body:
```json
{
	"name": "name",
	"user_id": 999
}
```
response:
```json
{
	"success": true,
	"data": {
		"id": 1,
		"name": "breakfast",
		"author_id": 4,
		"foods": [SERIALIZED FOODS],
		"total_calories": 100,
		"difficulty": 7.7
	}
}
```
## Get meal plan by id
### GET http://34.86.75.208/api/meal_plans/{id}/
response:
```json
{
	"success": true,
	"data": {
		"id": 1,
		"name": "breakfast",
		"author_id": 4,
		"foods": [SERIALIZED FOODS],
		"total_calories": 100,
		"difficulty": 7.7
	}
}
```
## Delete meal plan
### DELETE http://34.86.75.208/api/meal_plans/{id}/
response:
```json
{
	"success": true,
	"data": {
		"id": 1,
		"name": "breakfast",
		"author_id": 4,
		"foods": [SERIALIZED FOODS],
		"total_calories": 100,
		"difficulty": 7.7
	}
}
```
## Add food to a meal
### POST http://34.86.75.208/api/meal_plans/{meal_id}/add/{food_id}/
response:
```json
{
	"success": true,
	"data": {
		"id": 1,
		"name": "breakfast",
		"author_id": 4,
		"foods": [SERIALIZED FOODS],
		"total_calories": 100,
		"difficulty": 7.7
	}
}
```
