from flask import Flask
from payment import process_payment
from user import get_user

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def pay():
    return process_payment()

@app.route('/user/<id>', methods=['GET'])
def user(id):
    return get_user(id)

if __name__ == "__main__":
    app.run(debug=True)
