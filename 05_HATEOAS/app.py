from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample Data: F1 Teams and Drivers
teams = {
    1: {"name": "Red Bull Racing", "country": "Austria", "drivers": [1, 2]},
    2: {"name": "Mercedes-AMG Petronas", "country": "Germany", "drivers": [3, 4]},
    3: {"name": "Ferrari", "country": "Italy", "drivers": [5, 6]}
}

drivers = {
    1: {"name": "Max Verstappen", "team_id": 1, "number": 33},
    2: {"name": "Sergio Perez", "team_id": 1, "number": 11},
    3: {"name": "Lewis Hamilton", "team_id": 2, "number": 44},
    4: {"name": "George Russell", "team_id": 2, "number": 63},
    5: {"name": "Charles Leclerc", "team_id": 3, "number": 16},
    6: {"name": "Carlos Sainz", "team_id": 3, "number": 55}
}

# Helper function to generate HATEOAS links
def generate_links(resource, resource_id):
    return [
        {"rel": "self", "href": f"/{resource}/{resource_id}"},
        {"rel": "all", "href": f"/{resource}"}
    ]

# Team Resource
class TeamResource(Resource):
    def get(self, team_id=None):
        if team_id is None:
            # Return all teams with HATEOAS links
            return jsonify([
                {
                    "id": tid,
                    "name": data["name"],
                    "country": data["country"],
                    "drivers": [f"/driver/{did}" for did in data["drivers"]],
                    "links": generate_links("team", tid)
                } for tid, data in teams.items()
            ])

        if team_id not in teams:
            return {"message": "Team not found"}, 404

        team = teams[team_id]
        response = {
            "id": team_id,
            "name": team["name"],
            "country": team["country"],
            "drivers": [f"/driver/{did}" for did in team["drivers"]],
            "links": generate_links("team", team_id)
        }
        return jsonify(response)

# Driver Resource
class DriverResource(Resource):
    def get(self, driver_id=None):
        if driver_id is None:
            # Return all drivers with HATEOAS links
            return jsonify([
                {
                    "id": did,
                    "name": data["name"],
                    "number": data["number"],
                    "team": f"/team/{data['team_id']}",
                    "links": generate_links("driver", did)
                } for did, data in drivers.items()
            ])

        if driver_id not in drivers:
            return {"message": "Driver not found"}, 404

        driver = drivers[driver_id]
        response = {
            "id": driver_id,
            "name": driver["name"],
            "number": driver["number"],
            "team": f"/team/{driver['team_id']}",
            "links": generate_links("driver", driver_id)
        }
        return jsonify(response)

# Register API Resources
api.add_resource(TeamResource, "/team", "/team/<int:team_id>")
api.add_resource(DriverResource, "/driver", "/driver/<int:driver_id>")

if __name__ == "__main__":
    app.run(debug=True)
