








from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Table
from sqlalchemy import func, create_engine, text, and_, or_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
import datetime as dt
import json

engine = create_engine('sqlite+pysqlite:///foodlog.db')
MySession = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    meals = relationship("Meal")

    def __repr__(self):
        return "<User (name: {})>".format(self.name)

association_food_meal=Table('food_meal_mapping', Base.metadata,
                            Column('food_id', Integer, ForeignKey('food.food_id')),
                            Column('meal_id', Integer, ForeignKey('meal.meal_id')))

class Food(Base):
    __tablename__ = 'food'
    food_id = Column(Integer, primary_key=True)
    name = Column(String(300))
    energy = Column(Integer)
    fat = Column(Float)
    carb = Column(Float)
    protein = Column(Float)
    meals = relationship("Meal", secondary=association_food_meal, back_populates="foods")

    def __repr__(self):
        return "<Food (name: {}, food: {})>".format(self.name, self.energy)

class Meal(Base):
    __tablename__ = 'meal'
    meal_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    #user = relationship("User")
    foods = relationship("Food", secondary=association_food_meal, back_populates="meals")

    def __repr__(self):
        return "<Meal (name: {}, date: {})>".format(self.name, self.date)

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

def single_user_demo():
    u=User(name="Valaki Valeria")

    session.add(u)
    session.flush()
    session.commit()
    session.close()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session: Session = MySession()

    load_data(session)
    session.commit()


