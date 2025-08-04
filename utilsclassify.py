import sqlite3

def get_custom_categories():
    conn = sqlite3.connect("data/recipes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM categories ORDER BY name ASC")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
