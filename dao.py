from db import db, Meal_plan
from db import db, User
from db import db, Food

def get_all_meal_plans():
    return [m.serialize() for m in Meal_plan.query.all()]

def create_meal_plan(name, user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    new_meal_plan = Meal_plan(
        name = name,
        user_id = user_id
    )
    db.session.add(new_meal_plan)
    db.session.commit()
    return new_meal_plan.serialize()

def get_meal_plan(meal_plan_id):
    meal_plan = Meal_plan.query.filter_by(id = meal_plan_id).first()
    if meal_plan is None:
        return None
    return meal_plan.serialize()

def delete_meal_plan(meal_plan_id):
    meal_plan = Meal_plan.query.filter_by(id = meal_plan_id).first()
    if meal_plan is None:
        return None
    db.session.delete(meal_plan)
    db.session.commit()

    return meal_plan.serialize()

def create_user(username):
    new_user = User(
        username = username
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_user(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    return user.serialize()

def delete_user(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    db.session.delete(user)
    db.session.commit()
    return user.serialize()

def create_food(name, calories, difficulty):
    if difficulty > 10 or difficulty < 0:
        return None
    new_food = Food(
        name = name,
        calories = calories,
        difficulty = difficulty
    )

    db.session.add(new_food)
    db.session.commit()
    return new_food.serialize()


def get_all_foods():
    return [f.serialize() for f in Food.query.all()]

def assign_food(meal_plan_id, food_id):
    meal_plan = Meal_plan.query.filter_by(id = meal_plan_id).first()
    food = Food.query.filter_by(id = food_id).first()
    if meal_plan is None or food is None:
        return None

    meal_plan.foods.append(food)
    db.session.commit()
    return meal_plan.serialize()
