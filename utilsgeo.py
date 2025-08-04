import openrouteservice
from geopy.geocoders import Nominatim

ORS_API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjU3YmQzOTRlYWY1YTRjMjNhM2UxY2UzZTI5YzI1M2Q3IiwiaCI6Im11cm11cjY0In0="

categories = {
    'restaurant': 211,
    'cafe': 213,
    'bar': 212,
    'hotel': 581
}

def search_restaurants_nearby(address, type_lieu='restaurant', rayon=1500):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)
    if not location:
        return []

    latitude = location.latitude
    longitude = location.longitude

    client = openrouteservice.Client(key=ORS_API_KEY)

    category_id = categories.get(type_lieu, 211)

    try:
        pois = client.places(
            request='pois',
            geojson={"type": "Point", "coordinates": [longitude, latitude]},
            buffer=rayon,
            filters={'category_ids': [category_id]},
            limit=10
        )

        results = []
        for feature in pois['features']:
            results.append({
                'name': feature['properties'].get('name', type_lieu),
                'lat': feature['geometry']['coordinates'][1],
                'lon': feature['geometry']['coordinates'][0]
            })
        return results
    except Exception as e:
        print("ORS error:", e)
        return []
