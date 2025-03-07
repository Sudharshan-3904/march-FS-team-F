from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
data = [
    {"ID": 1, "Name": "Alice"},
    {"ID": 2, "Name": "Bob"},
    {"ID": 3, "Name": "Charlie"}
]

@app.route('/get_ids', methods=['GET'])
def get_ids():
    # Returns the list of all IDs
    ids = [entry["ID"] for entry in data]
    return jsonify({"IDs": ids})

@app.route('/validate_id/<int:id>', methods=['GET'])
def validate_id(id):
    # Validates if the given ID exists in the data
    ids = [entry["ID"] for entry in data]
    if id in ids:
        return jsonify({"Valid": True, "Message": f"ID {id} is valid."})
    return jsonify({"Valid": False, "Message": f"ID {id} is not in the list."}), 400

if __name__ == '__main__':
    app.run(debug=True)
