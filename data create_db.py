import sqlite3

conn = sqlite3.connect("data/recipes.db")
cursor = conn.cursor()

# Table des recettes
cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    ingredients TEXT,
    instructions TEXT,
    category TEXT,
    image_url TEXT
)
""")

# Table des catégories personnalisées
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

# Tu peux ajouter des catégories personnalisées ici :
default_categories = ['Healthy', 'Fast', 'Vegetarian', 'World Cuisine', 'Dessert']
for cat in default_categories:
    cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (cat,))

conn.commit()
conn.close()
print("? Base de données créée avec succès.")
