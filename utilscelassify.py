import sqlite3

DB_PATH = 'recipes.db'

def get_custom_categories():
    """Retourne une liste de noms de cat�gories"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM categories ORDER BY name")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def add_category(name):
    """Ajoute une nouvelle cat�gorie si elle n'existe pas"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def edit_category(old_name, new_name):
    """Renomme une cat�gorie existante"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE categories SET name = ? WHERE name = ?", (new_name, old_name))
    conn.commit()
    conn.close()
