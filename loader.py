from orm_demo import Meal, User, Food
import json

def load_foods():
    with open("foods_short.json") as food_file:
        dump = json.load(food_file)
    res=[Food(name=r['name'], energy=r['energy'], fat=r['fat'], protein=r['protein'], carb=r['carb']) for r in dump]
    return res

def load_meals(foods):
    food_size=len(foods)
    with open("meals.json") as food_file:
        r = json.load(food_file)
    r2=[Meal(name= e[0], date= dt.datetime.strptime(e[1], '%Y-%m-%d %H:%M:%S'),
             foods=[foods[e[2][0]%food_size], foods[e[2][1]%food_size]]) for e in r]
    return r2

def load_data(sess):
    foods=load_foods()
    meals=load_meals(foods)
    sess.add_all(foods)
    sess.add_all(meals)
    sess.flush()
    sess.commit()