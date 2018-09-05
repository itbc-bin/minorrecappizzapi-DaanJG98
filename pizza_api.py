from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
            {"name": "tonno", "ingredienten":["tomaat", "kaas", "tonijn"]},
            {"name": "salami", "ingredienten":["tomaat", "kaas", "salami"]},
            {"name": "hawaii", "ingredienten":["tomaat", "kaas", "ham", "ananas"]}
            ]


@app.route('/', methods=["GET"])
def get_pizza():
    return jsonify({"pizzaDB": pizzaDB})

@app.route("/<string:name>", methods=['GET'])
def get_one_pizza(name):
    resultPizza = [pizza for pizza in pizzaDB if pizza['name'] == name]
    return jsonify({"pizzaDB": resultPizza})

@app.route("/<string:name>/ingredienten", methods=['GET'])
def get_ingredienten(name):
    resultPizza = [pizza['ingredienten'] for pizza in pizzaDB if pizza['name'] == name]
    return jsonify({"pizzaDB": resultPizza})

@app.route("/", methods=['POST'])
def addOnePizza():
    # pizza = {
    #     'name': request.json['name'],
    #     'ingredienten': request.json['ingredienten']
    # }
    pizzaDB.append(request.json)
    return jsonify({'pizzaDB': pizzaDB})

# add one or more ingredients to a single pizza
@app.route("/add_ingredient/<string:name>", methods=['POST'])
def add_ingredients(name):
    ingredients = request.args.get('ingredients').split(',')
    for pizza in pizzaDB:
        if pizza['name'] == name:
            for ingredient in ingredients:
                pizza['ingredienten'].append(ingredient)
    return jsonify({'pizzaDB': pizzaDB})

# add a price to a pizza
@app.route("/add_price/<string:name>", methods=['POST'])
def add_price(name):
    price = request.args.get('price')
    for pizza in pizzaDB:
        if pizza['name'] == name:
            pizza.update({'price': price})
    return jsonify({'pizzaDB': pizzaDB})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
