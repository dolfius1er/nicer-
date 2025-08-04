import requests

def search_recipes(query):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    response = requests.get(url)
    if response.status_code != 200:
        return []

    data = response.json()
    results = []

    if data["meals"] is None:
        return []

    for meal in data["meals"]:
        results.append({
            "title": meal.get("strMeal"),
            "category": meal.get("strCategory"),
            "image": meal.get("strMealThumb"),
            "instructions": meal.get("strInstructions"),
            "ingredients": get_ingredients(meal)
        })

    return results

def get_ingredients(meal):
    ingredients = []
    for i in range(1, 21):  # TheMealDB has 20 ingredient slots max
        ingredient = meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")
        if ingredient and ingredient.strip():
            ingredients.append(f"{ingredient} - {measure}")
    return ingredients
