from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask' # version on localhost db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@mysql-db/flask' # version on docker db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
#
ma = Marshmallow(app)


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    pets = db.relationship('Pet', backref='owner', lazy=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner  # this is instance of owner

# first creating table in db ( need to install <brew install mysql>) after in terminal
# -> Python3 -> from app import db
# from app import db
# with app.app_context():
#    db.create_all()


with app.app_context():
    db.create_all()


class PetSchema(ma.Schema):
    model = Pet

    class Meta:
        fields = ('id', 'name', 'age')


class OwnerSchema(ma.Schema):
    model = Owner
    pets = fields.Nested(PetSchema(many=True))

    class Meta:
        fields = ('id', 'name', 'address', 'pets')


owner_schema = OwnerSchema()
owners_schema = OwnerSchema(many=True)

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)


@app.route('/add-owner', methods=['POST'])
def add_owner():
    name = request.json['name']
    address = request.json['address']
    print(name, address)
    owner = Owner(name, address)
    # print(owner)
    db.session.add(owner)
    db.session.commit()
    # return jsonify({"Hello": "World"})
    return owner_schema.jsonify(owner)


@app.route('/add-pet', methods=['POST'])
def add_pet():
    name = request.json['name']
    age = request.json['age']
    owner_id = request.json['owner_id']
    owner = db.get_or_404(Owner, owner_id)
    print(name, age, owner.name)

    pet = Pet(name, age, owner)
    # print(pet)
    db.session.add(pet)
    db.session.commit()
    # return jsonify({"Hello": "World"})
    return pet_schema.jsonify(pet)


@app.route('/get', methods=['GET'])
def get_all_owners():
    owners = Owner.query.all()
    # return jsonify({"Hello": "ALL Worldes -all"})
    return owners_schema.jsonify(owners)


@app.route('/get/<id>', methods=['GET'])
def get_owner_data(id):
    # pets = Pet.query.filter(Pet.owner_id==id).all() # can use filter OR filter_by
    pets = Pet.query.filter_by(owner_id=id).all()
    owner = db.get_or_404(Owner, id)
    return owner_schema.jsonify(owner)
    # return pets_schema.jsonify(pets)


# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/

if __name__ == '__main__':
    # app.run(debug=False)
    print("Server started")
    app.run(debug=True, host='0.0.0.0', port=5000)
