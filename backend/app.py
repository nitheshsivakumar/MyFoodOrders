from flask import Flask
from vendor_routes import vendor_bp

app = Flask(__name__)

# Register the vendor routes
app.register_blueprint(vendor_bp)

@app.route('/')
def home():
    return {"message": "Welcome to MyFoodOrders Admin API!"}

if __name__ == '__main__':
    app.run(debug=True)

