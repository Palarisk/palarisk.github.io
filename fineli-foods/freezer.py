from flask_frozen import Freezer
from app import app, Food

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def food():
    for food in Food.query.all():
        yield { 'FOODID': food.FOODID }



if __name__ == '__main__':
    freezer.freeze()
