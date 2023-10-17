from flask import Flask, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__)

def get_count_from_file():
    with open("count.txt", "r") as file:
        return int(file.read().strip())

def write_count_to_file(count):
    with open("count.txt", "w") as file:
        file.write(str(count))

@app.route('/post/', methods=['POST'])
@cross_origin()
def post_request():
    count = get_count_from_file()
    count -= 1
    write_count_to_file(count)
    count = get_count_from_file()
    return jsonify({'count': count})

@app.route('/get/', methods=['GET'])
@cross_origin()
def get_request():
    count = get_count_from_file()
    return jsonify({'count': count})

if __name__ == '__main__':
    app.run(debug=True)
