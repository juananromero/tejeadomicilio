print("Hola Tejedoras")
from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = [
  {
    'id': 1,
    'title': "Producto 1",
    'precio': 33.44
  },
  {
    'id': 2,
    'title': "Producto 2",
    'precio': 55.66
  },
  {
    'id': 3,
    'title': "Producto 3",
    'precio': 77.88
  }
]
@app.route("/")
def hello_world():
    return render_template('home.html', products=PRODUCTS)

@app.route("/api/products")
def list_products():
    return jsonify(PRODUCTS)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
