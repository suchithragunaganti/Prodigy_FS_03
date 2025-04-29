
from flask import Flask, render_template_string

app = Flask(__name__)

# Expanded product list with working image URLs
products = [
    {
        "id": 1,
        "name": "Organic Honey",
        "description": "Pure honey harvested from local farms. 500ml glass jar.",
        "price": 12.99,
        "image": "https://1.bp.blogspot.com/-GxoPKQaVh_U/VvpsdVipQBI/AAAAAAAAAIo/7ICTWPv2RpAC2ElhyOJBobP4onWsovt9QCKgB/s1600/453744653.jpg"
    },
    {
        "id": 2,
        "name": "Herbal Soap",
        "description": "Handcrafted soap made with natural herbs and essential oils.",
        "price": 5.49,
        "image": "https://beautycrafter.com/wp-content/uploads/2015/05/potted-herbs-for-scented-soaps.jpg"
    },
    {
        "id": 3,
        "name": "Coffee Beans",
        "description": "Locally roasted Arabica beans. Medium roast. 250g bag.",
        "price": 9.99,
        "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 4,
        "name": "Handmade Mug",
        "description": "Ceramic coffee mug handmade by local artisans.",
        "price": 14.00,
        "image": "https://i.etsystatic.com/28554635/r/il/02ffa5/3008250858/il_fullxfull.3008250858_enac.jpg"
    },
    {
        "id": 5,
        "name": "Scented Candle",
        "description": "Soy wax candle with lavender and eucalyptus scent.",
        "price": 8.75,
        "image": "https://khalisafragrance.com/wp-content/uploads/2023/02/candle.jpg"
    },
    {
        "id": 6,
        "name": "Jute Tote Bag",
        "description": "Eco-friendly jute bag, perfect for groceries or casual use.",
        "price": 6.50,
        "image": "https://musajute.com/wp-content/uploads/2021/08/U9d07de813b2449f287c0fb4b5906ad56L.jpg"
    }
]

# Home page HTML template
home_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Local Store</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f5f5f5; }
        h1 { color: #333; }
        .products { display: flex; gap: 20px; flex-wrap: wrap; }
        .product {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            width: 250px;
            background: #fff;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
        }
        .product img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 5px;
        }
        .product h2 {
            font-size: 18px;
            margin: 10px 0 5px;
        }
        a {
            text-decoration: none;
            color: #007BFF;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Welcome to Local Store</h1>
    <div class="products">
        {% for product in products %}
        <div class="product">
            <img src="{{ product.image }}" alt="{{ product.name }}">
            <h2>{{ product.name }}</h2>
            <p>{{ product.description }}</p>
            <p><strong>${{ product.price }}</strong></p>
            <a href="/product/{{ product.id }}">View Details</a>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

# Product detail HTML template
product_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ product.name }}</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f9f9f9; }
        .container {
            max-width: 600px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        img {
            width: 100%;
            height: 300px;
            object-fit: cover;
            border-radius: 5px;
        }
        h1 { margin-top: 0; }
        a {
            display: inline-block;
            margin-top: 10px;
            color: #007BFF;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ product.name }}</h1>
        <img src="{{ product.image }}" alt="{{ product.name }}">
        <p>{{ product.description }}</p>
        <p><strong>Price: ${{ product.price }}</strong></p>
        <a href="/">← Back to Store</a>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(home_template, products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template_string(product_template, product=product)

if __name__ == '__main__':
    app.run(debug=True)
