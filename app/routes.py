from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.breed = description

PLANETS = [
    Planet(1, 'Mercury', ''),
    Planet(2, 'Venus', ''),
    Planet(3, 'Earth', ''),
    Planet(4, 'Mars', ''),
    Planet(5, 'Jupiter', ''),
    Planet(6, 'Saturn', ''),
    Planet(7, 'Uranus' ''),
    Planet(8, 'Neptune', ''),
    Planet(9, 'Pluto', ''))
]



planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def get_all_planets():
    planets_response = []
    for planet in PLANETS:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "age": planet.description,
        })

    return jsonify(planets_response)