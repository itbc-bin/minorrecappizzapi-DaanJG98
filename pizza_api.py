from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
            {"name": "tonno", "ingredienten":["tomaat", "kaas", "tonijn"], "price": 100},
            {"name": "salami", "ingredienten":["tomaat", "kaas", "salami"], "price": 69},
            {"name": "hawaii", "ingredienten":["tomaat", "kaas", "ham", "ananas"], "price": 5}
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

@app.route("/<string:name>", methods=['PUT'])
def put_pizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    resultPizza[0]['name'] = request.json['name']
    return jsonify({'pizzaDB': pizzaDB})

@app.route("/<string:name>", methods=['DELETE'])
def del_pizza(name):
    resultPizza = [pizza for pizza in pizzaDB if pizza['name'] == name]
    pizzaDB.remove(resultPizza)
    return jsonify({'pizzaDB': pizzaDB})

@app.route("/<string:name>/update_price", methods=['PUT'])
def update_price(name):
    resultPizza = [pizza for pizza in pizzaDB if pizza['name'] == name]
    resultPizza[0]['price'] = request.json['price']
    return jsonify({'pizzaDB': pizzaDB})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
