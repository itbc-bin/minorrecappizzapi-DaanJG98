from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
            {"name": "tonno"},
            {"name": "salami"},
            {"name": "hawaii"}
            ]


@app.route('/', methods=["GET"])
def get_pizza():
    return jsonify({"pizzaDB": pizzaDB})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
