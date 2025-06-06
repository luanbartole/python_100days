from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql import func, select
import random

app = Flask(__name__)

# Define custom SQLAlchemy base class
class Base(DeclarativeBase):
    pass

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Define Cafe model/table
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    # Convert model to dictionary
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Create database tables
with app.app_context():
    db.create_all()

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Get one random cafe
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(select(Cafe).order_by(func.random()))
    random_cafe = result.scalars().first()
    return jsonify(cafe=random_cafe.to_dict())

# Get all cafes
@app.route("/all")
def get_all_cafes():
    result = db.session.execute(select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(all_cafes=[cafe.to_dict() for cafe in all_cafes])

# Search cafe by location
@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    result = db.session.execute(select(Cafe).where(Cafe.location == query_location))
    cafes_at_location = result.scalars().all()
    if not cafes_at_location:
        return jsonify(error={"Not found": "Cafe with that Location not found."}), 404
    return jsonify(all_cafes=[cafe.to_dict() for cafe in cafes_at_location])

# Add a new cafe
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        seats=request.form.get("seats"),
        has_toilet=bool(int(request.form.get("has_toilet"))),
        has_wifi=bool(int(request.form.get("has_wifi"))),
        has_sockets=bool(int(request.form.get("has_sockets"))),
        can_take_calls=bool(int(request.form.get("can_take_calls"))),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe"}), 200

# Update coffee price by cafe ID
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    new_price = request.args.get("coffee_price")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not found": "Cafe with that ID not found."}), 404
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the coffee price"}), 200

# Delete a cafe by ID with API key
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != "TopSecretAPIKey":
        return jsonify(error={"Forbidden": "That is not allowed. Make sure you have the correct api_key."}), 403
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not found": "Cafe with that ID not found."}), 404
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host="localhost", port="5000")
