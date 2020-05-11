from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json
import copy

from models.float_rod import FloatRod

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class FloatRodSet(FloatRod, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Enum, unique=False)
    length_in_meters = db.Column(db.Float, unique=False)
    folded_length_in_meters = db.Column(db.Float, unique=False)
    number_of_sections = db.Column(db.Integer, unique=False)
    weight_in_kg = db.Column(db.Float, unique=False)
    type_of_fishing_float = db.Column(db.String, unique=False)

    price = db.Column(db.Float, unique=False)

    def __init__(self, season, length_in_meters, folded_length_in_meters, number_of_sections, weight_in_kg,
                 type_of_fishing_float, price):
        super().__init__(season, length_in_meters, folded_length_in_meters, number_of_sections, weight_in_kg,
                         type_of_fishing_float)
        self.price = price


class FloatRodSetSchema(ma.Schema):
    class Meta:
        fields = ('season', 'length_in_meters', 'folded_length_in_meters', 'number_of_sections', 'weight_in_kg',
                  'type_of_fishing_float', 'price')


float_rod_set_schema = FloatRodSetSchema()
float_rod_sets_schema = FloatRodSetSchema(many=True)


@app.route("/float_rod_set", methods=["POST"])
def add_float_rod_set():
    float_rod_set = FloatRodSet(request.json['season'], request.json['length_in_meters'],
                                request.json['folded_length_in_meters'], request.json['number_of_sections'],
                                request.json['weight_in_kg'], request.json['type_of_fishing_float'],
                                request.json['price'])

    db.session.add(float_rod_set)
    db.session.commit()
    return float_rod_set_schema.jsonify(float_rod_set)


@app.route("/float_rod_set", methods=["GET"])
def get_float_rod_sets():
    all_float_rod_sets = FloatRodSet.query.all()
    result = float_rod_sets_schema.dump(all_float_rod_sets)
    return jsonify({'float_rod_sets': result})


@app.route("/float_rod_set<id>", methods=["GET"])
def get_float_rod_set(id):
    float_rod_set = FloatRodSet.query.get(id)
    if not float_rod_set:
        abort(404)
    return float_rod_set_schema.jsonify(float_rod_set)


@app.route("/float_rod_set<id>", methods=["PUT"])
def update_float_rod_set(id):
    float_rod_set = FloatRodSet.query.get(id)
    if not float_rod_set:
        abort(404)
    old_float_rod_set = copy.deepcopy(float_rod_set)
    float_rod_set.season = request.json['season']
    float_rod_set.length_in_meters = request.json['length_in_meters']
    float_rod_set.folded_length_in_meters = request.json['folded_length_in_meters']
    float_rod_set.number_of_sections = request.json['number_of_sections']
    float_rod_set.weight_in_kg = request.json['weight_in_kg']
    float_rod_set.type_of_fishing_float = request.json['type_of_fishing_float']
    float_rod_set.price = request.json['price']
    db.session.commit()
    return float_rod_set_schema.jsonify(old_float_rod_set)


@app.route("/float_rod_set<id>", methods=["DELETE"])
def delete_float_rod_set(id):
    float_rod_set = FloatRodSet.query.get(id)
    if not float_rod_set:
        abort(404)
    db.session.delete(float_rod_set)
    db.session.commit()
    return float_rod_set_schema.jsonify(float_rod_set)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
