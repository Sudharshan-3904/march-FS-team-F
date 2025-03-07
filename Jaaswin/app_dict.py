from flask  import Flask , request , jsonify

app = Flask(__name__)

@app.route("/Indroduction/<name>/<age>", methods=["GET"])
def index(name,age):
    return f"👋 Hi, I’m  {name.capitalize()} and {age} years"

@app.route("/Search", methods=["GET", "POST"])
def search():
    payload = request.json
    i_d  = request.args.get("id")
    age = request.args.get("age")
    name = request.args.get("name")
    res = {"NAme": name, "age": age, "ID": i_d}
    print(res)
    return jsonify(res)

if __name__ == '__main__':
    app.run(port=3025, debug=True)
    print("Server is running...")

