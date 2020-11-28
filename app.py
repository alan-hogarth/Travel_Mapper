from flask import Flask, render_template

from controllers.city_controller import cities_blueprint
from controllers.country_controller import countries_blueprint
from controllers.user_controller import users_blueprint
from controllers.visit_controller import trips_blueprint

app = Flask(__name__)

app.register_blueprint(trips_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(countries_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)