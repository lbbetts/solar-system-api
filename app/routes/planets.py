from app import db
from app.routes import planets_bp
from app.models.planet_model import Planet
from flask import Blueprint, jsonify, abort, make_response, request

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

PLANETS = [
    Planet(1, 'Mercury', 'Planet of Communication'),
    Planet(2, 'Venus', 'Planet of Love and Money'),
    Planet(3, 'Earth', 'Home'),
    Planet(4, 'Mars', 'Planet of Passion'),
    Planet(5, 'Jupiter', 'Planet of Luck'),
    Planet(6, 'Saturn', 'Planet of Karma'),
    Planet(7, 'Uranus', 'Planet of Rebellion'),
    Planet(8, 'Neptune', 'Planet of Illusion'),
    Planet(9, 'Pluto', 'Planet of Power')
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
def handle_get_planet(id):

    #return dict
    planet = validate_planet(id)

    planet = Planet.query.get(id)

    if request.method == "GET":
        return {
            "name": planet.name,
            "id": planet.id,
            "description": planet.description
        }

@planets_bp.route('/planet', methods=['PUT'])
def create_planet():
    planet = Planet.query.get(id)
    request_body = request.get_json()

    planet.name=request_body["name"],
    planet.id=request_body["id"],
    planet.description=request_body["description"]
    
    db.session.commit()

    return make_response(f"Planet {planet.name} has been successfully created!", 201)

@planets_bp.route('/<id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planet.query.get(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.name} has been successfully delete!", 201)

#validation func
def validate_planet(id):

    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    
    return planet


    #invalid id type
    #try:
    #    planet_id = int(id)
    #except ValueError:
    #    return {
    #        "message": "Invalid planet id"
    #    }, 400

    ##id not found
    #for planet in PLANETS:
    #    if planet_id == planet.id:
    #        return vars(planet)
    #abort(make_response(jsonify(description="Planet not found"),404))