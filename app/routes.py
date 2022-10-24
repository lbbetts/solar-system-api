from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

PLANETS = [
    Planet(1, 'Mercury', ''),
    Planet(2, 'Venus', ''),
    Planet(3, 'Earth', ''),
    Planet(4, 'Mars', ''),
    Planet(5, 'Jupiter', ''),
    Planet(6, 'Saturn', ''),
    Planet(7, 'Uranus', ''),
    Planet(8, 'Neptune', ''),
    Planet(9, 'Pluto', '')
]



planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def get_all_planets():
    planets_response = []
    for planet in PLANETS:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
        })

    return jsonify(planets_response)

@planets_bp.route('/<id>', methods=['GET'])
def get_one_planet(id):
    #return dict
    planet = validate_planet(id)
    return planet

#validation func
def validate_planet(id):
    #invalid id type
    try:
        planet_id = int(id)
    except ValueError:
        return {
            "message": "Invalid planet id"
        }, 400

    #id not found
    for planet in PLANETS:
        if planet_id == planet.id:
            return vars(planet)
    abort(make_response(jsonify(description="Planet not found"),404))