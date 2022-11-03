from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet_model import Planet
from app import db


planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

# class Planet:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# PLANETS = [
#     Planet(1, 'Mercury', 'Planet of Communication'),
#     Planet(2, 'Venus', 'Planet of Love and Money'),
#     Planet(3, 'Earth', 'Home'),
#     Planet(4, 'Mars', 'Planet of Passion'),
#     Planet(5, 'Jupiter', 'Planet of Luck'),
#     Planet(6, 'Saturn', 'Planet of Karma'),
#     Planet(7, 'Uranus', 'Planet of Rebellion'),
#     Planet(8, 'Neptune', 'Planet of Illusion'),
#     Planet(9, 'Pluto', 'Planet of Power')
# ]


@planets_bp.route('', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "title": planet.title,
            "description": planet.description,
        })

    return jsonify(planets_response)

    # planets = Planet.query.all()
    # planets_response = []

    # planet_title_query = request.args.get("title")

    # if planet_title_query:
    #     planets = Planet.query.filter_by(title=planet_title_query)
    # else:
    #     planets = Planet.query.all()

    # for planet in planets:
    #     planets_response.append({
    #         "id": planet.id,
    #         "title": planet.title,
    #         "description": planet.description
    #         })
    # return jsonify(planets_response)  

@planets_bp.route('/<id>', methods=['GET'])
def get_one_planet(id):
    # return dict
    planet = validate_planet(id)

    planet = Planet.query.get(id)

    if request.method == "GET":
        return {
            "title": planet.title,
            "id": planet.id,
            "description": planet.description
        }
    return planet

@planets_bp.route('/<id>', methods=['PUT'])
def update_planet(id):
    request_body = request.get_json()
    if "title" not in request_body or "description" not in request_body:
        return make_response("Invalid Request", 400)
        
    planet = validate_planet(id)

    planet = Planet.query.get(id)


    planet.title=request_body["title"],
    planet.description=request_body["description"]
    
    db.session.commit()

    return make_response(f"Planet {planet.title} has been successfully updated!", 201)

@planets_bp.route('', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    if "title" not in request_body or "description" not in request_body:
        return make_response("Invalid Request", 400)

    new_planet = Planet(
        title=request_body["title"],
        description=request_body["description"]
    )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(
        f"Planet {new_planet.title} created", 201
    )      
    # planet = Planet.query.get(id)
    # request_body = request.get_json()

    # planet.title=request_body["title"],
    # # planet.id=request_body["id"],
    # planet.description=request_body["description"]
    
    # db.session.commit()

    # return make_response(f"Planet {planet.title} has been successfully created!", 201)

@planets_bp.route('/<id>', methods=['DELETE'])
def delete_planet(id):
    planet = validate_planet(id)

    planet = Planet.query.get(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.title} has been successfully deleted!", 201)

#validation func
def validate_planet(id):
    #invalid id type
    try:
        planet_id = int(id)
    except ValueError:
        abort(make_response(jsonify(description="Planet invalid"),400))

    #id not found
    planets = Planet.query.all()
    
    for planet in planets:
        if planet_id == planet.id:
            return vars(planet)
    abort(make_response(jsonify(description="Planet not found"),404))


    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # if not test_config:
    #     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    #         "SQLALCHEMY_DATABASE_URI")
    # else:
    #     app.config["TESTING"] = True
    #     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    #         "SQLALCHEMY_TEST_DATABASE_URI")