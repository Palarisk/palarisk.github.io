from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foods.db'
db = SQLAlchemy(app)

# A few extra imports
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Food(db.Model):
  __tablename__ = 'foods'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  FOODID = db.Column(db.Integer, primary_key=True)
  # this model has a relationship with the Score model
#  nutrs = db.relationship('Nutrs')

#class Nutr(db.Model):
#  __tablename__ = 'nutrs'
#  __table_args__ = {
#    'autoload': True,
#    'autoload_with': db.engine
#  }
  # You add ForeignKey(schools.dbn) when declaring a column
  # to say that the dbn column you're talking about (dbn = )
  # is connected to the dbn column in the schools table (schools.dbn)
#  FOODID = db.Column(db.Integer, ForeignKey('foods.FOODID'), primary_key=True)

#Nää on nyt sekasin että mitä mikin on:
@app.route("/")
def start():
  foods = Food.query.all()
  return render_template("list.html", foods=foods)

@app.route("/foods/")
def foods():
  foods = Food.query.all()
  return render_template("list.html", foods=foods)

@app.route("/foods/<FOODID>/")
def food(FOODID):
  food = Food.query.filter_by(FOODID=FOODID).first()
  return render_template("show.html", food=food)

# @app.route("/search")
# def search():
#   name = request.args.get('query')
#   fineli = School.query.filter(School.school_name.contains(name)).all()
#   return render_template("list.html", fineli=fineli)


# If this is running from the command line
# do something
if __name__ == '__main__':
  app.run(debug=True)
