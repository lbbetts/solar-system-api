from flask import Blueprint

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
    for planets in PLANETS:
        dog_response.append({
            "id": dog.id,
            "name": dog.name,
            "age": dog.age,
            "breed": dog.breed,
            "gender": dog.gender
        })

    return jsonify(dog_response)