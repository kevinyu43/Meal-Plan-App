# Meal-Plan-App
App that allows users to create meal plans.

## Get all meal plans
### GET http://34.86.75.208/api/foods/
reponse: 
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

## Create a food 
### POST http://34.86.75.208/api/foods/
request body:
{
	"name": <USER INPUT>,
	"calories": <USER INPUT>,
	"difficulty": <NUMBER BETWEEN 0 AND 10>
}/
reponse:
