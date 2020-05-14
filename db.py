from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

food_association = db.Table("association", db.Model.metadata,
    db.Column("mean_plan_id", db.Integer, db.ForeignKey("food.id")),
    db.Column("food_id", db.Integer, db.ForeignKey("meal_plan.id"))
)
class Meal_plan(db.Model):
    __tablename__ = "meal_plan"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    foods = db.relationship("Food", secondary=food_association, back_populates="plans")

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.author = kwargs.get("user_id", "")

    def total_calories(self):
        sum = 0
        for f in self.foods:
            sum = sum + f.getCalories()
        return sum

    def average_difficulty(self):
        sum = 0
        n = 0
        for f in self.foods:
            sum = sum + f.getDifficulty()
            n = n + 1
        if n == 0:
            return 0
        return sum / n
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "author_id": self.author,
            "foods": [f.short_serialize() for f in self.foods],
            "total_calories": self.total_calories(),
            "difficulty": self.average_difficulty()
        }


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    mean_plans = db.relationship("Meal_plan", cascade="delete")

    def __init__(self, **kwargs):
        self.username = kwargs.get("username", "")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "mean_plans": [m.serialize() for m in self.mean_plans]
        }


class Food(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    plans = db.relationship("Meal_plan", secondary=food_association, back_populates="foods")
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.difficulty = kwargs.get("difficulty", "")
        self.calories = kwargs.get("calories", "")

    def getDifficulty(self):
        return self.difficulty

    def getCalories(self):
        return self.calories

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "difficulty": self.difficulty,
            "calories": self.calories
        }
    def short_serialize(self):
        return self.name
