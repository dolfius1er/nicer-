from flask import Flask, render_template, request
import sqlite3

try:
    from utils.geo import search_restaurants_nearby
    from utils.api import search_recipes
    from utils.classify import get_custom_categories
except ModuleNotFoundError as e:
    print(f"Warning: {e}. Some modules are missing.")
    search_restaurants_nearby = lambda *args, **kwargs: []
    search_recipes = lambda *args, **kwargs: []
    get_custom_categories = lambda: []

app = Flask(__name__)

# === ROUTE PRINCIPALE ===
@app.route('/')
def index():
    return render_template('index.html')

# === RECHERCHE DE RECETTES ===
@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    results = []
    query = ''
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            results = search_recipes(query)
    return render_template('recipes.html', results=results, query=query)

# === RECHERCHE DE RESTAURANTS ===
@app.route('/restaurants', methods=['GET', 'POST'])
def restaurants():
    results = []
    address = ''
    type_cuisine = ''
    if request.method == 'POST':
        address = request.form.get('address')
        type_cuisine = request.form.get('type_cuisine')
        if address and type_cuisine:
            results = search_restaurants_nearby(address, type_cuisine)
    return render_template('restaurants.html', results=results, address=address, type_cuisine=type_cuisine)

# === CATEGORIES PERSONNALISEES ===
@app.route('/categories')
def categories():
    cats = get_custom_categories()
    return render_template('categories.html', categories=cats)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"
