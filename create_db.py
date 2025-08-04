import sqlite3

def create_database():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    # Création de la table catégories
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')

    # Exemples de catégories par défaut
    default_categories = [
        "Asian", "Vegetarian", "Dessert", "Italian",
        "Fast Food", "Healthy", "Grill", "Seafood"
    ]

    for cat in default_categories:
        cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (cat,))

    conn.commit()
    conn.close()
    print("? Base de données créée avec succès.")

if __name__ == "__main__":
    create_database()
