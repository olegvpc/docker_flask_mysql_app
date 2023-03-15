from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/get', methods=['GET'])
def get_all_owners():
    # owners = Owner.query.all()
    return jsonify({"Hello": "World"})


if __name__ == '__main__':
    # app.run(debug=False)
    print("Server started")
    app.run(debug=True, host='0.0.0.0', port=5000)
