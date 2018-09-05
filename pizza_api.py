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

@app.route("/<string:name>", methods=['GET'])
def get_one_pizza(name):
    resultPizza = [pizza for pizza in pizzaDB if pizza['name'] == name]
    return jsonify({"pizzaDB": resultPizza})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
