from flask import Flask, request
import dao
import json
from db import db

app = Flask(__name__)
db_filename = "plans.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


#response methods
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

@app.route("/api/meal_plans/")
def get_meal_plans():
    return success_response(dao.get_all_meal_plans())

@app.route("/api/meal_plans/", methods = ["POST"])
def create_meal_plan():
    body = json.loads(request.data)
    meal_plan = dao.create_meal_plan(
        body.get("name"),
        body.get("user_id")
    )

    if meal_plan is None:
        return failure_response("User not found!")
    return success_response(meal_plan, 201)

@app.route("/api/meal_plans/<int:meal_plan_id>/add/<int:food_id>/", methods = ["POST"])
def add_food(meal_plan_id, food_id):
    meal_plan = dao.assign_food(meal_plan_id, food_id)
    if meal_plan is None:
        return failure_response("Either the meal plan or food did not existe!")
    return success_response(meal_plan)

@app.route("/api/meal_plans/<int:meal_plan_id>/", methods = ["GET"])
def get_meal_plan(meal_plan_id):
    meal_plan = dao.get_meal_plan(meal_plan_id)
    if meal_plan is None:
        return failure_response("Meal plan not found!")
    return success_response(meal_plan)

@app.route("/api/meal_plans/<int:meal_plan_id>/", methods = ["DELETE"])
def delete_meal_plan(meal_plan_id):
    meal_plan = dao.delete_meal_plan(meal_plan_id)
    if meal_plan is None:
        return failure_response("Meal plan not found!")
    return success_response(meal_plan)

@app.route("/api/users/", methods = ["POST"])
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        username = body.get("username")
    )
    return success_response(user)

@app.route("/api/users/<int:user_id>/")
def get_user(user_id):
    user = dao.get_user(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route("/api/users/<int:user_id>/", methods = ["DELETE"])
def delete_user(user_id):
    user = dao.delete_user(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route("/api/foods/")
def get_foods():
    return success_response(dao.get_all_foods())

@app.route("/api/foods/", methods = ["POST"])
def create_food():
    body = json.loads(request.data)
    food = dao.create_food(
        name = body.get("name"),
        calories = body.get("calories"),
        difficulty = body.get("difficulty")
    )
    if food is None:
        return failure_response("Difficulty must be between 1 and 10")
    return success_response(food)






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
