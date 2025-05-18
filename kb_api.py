from flask import Flask, jsonify
from collections import defaultdict

app = Flask(__name__)

# Sample KB data for properties (list)
properties = [
    {
        "primary_name": "Barbeque Nation Bangalore",
        "address": "Koramangala",
        "city": "Bengaluru"
    },
    {
        "primary_name": "Barbeque Nation Delhi",
        "address": "Connaught Place",
        "city": "New Delhi"
    }
]

@app.route("/properties", methods=["GET"])
def get_properties():
    # Group properties by city
    grouped = defaultdict(list)
    for prop in properties:
        city = prop.get("city", "Unknown").strip()
        grouped[city].append(prop)
    return jsonify(grouped)

if __name__ == "__main__":
    app.run(port=5000)
