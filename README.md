# Meal-Plan-App
App that allows users to create meal plans.

## Get all meal plans
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
request body:
```json
{
	"name": name,
	"calories": number,
	"difficulty": number between 1 and 10
}
``` 
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
## Get a user by ID
### GET http://34.86.75.208/api/users/{id}/
response:
```json
{
	"success": true,
	"data": [
		{
			"id": 1,
			"username": "kevin12",
			"meal_plans": SERIALIZED MEAL PLANS
		}
	]
}
```
## Create User

