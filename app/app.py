from flask import Flask, jsonify, request

app = Flask(__name__)

incomes_r = [{'description': 'rating', 'amount': 'AA'}]
incomes_dly = [{'description': 'dly', 'amount': '0.030'}]
incomes_dft = [{'description': 'dft', 'amount': '0.080'}]

@app.route('/rating',methods=["POST", "GET"])
def get_rating():
  content = []
  if request.method == "GET":
    content = incomes_r
    # if request.headers.get("accept") == "application/json":
    # content = request.get_json()
  return jsonify(content)


@app.route('/default',methods=["POST", "GET"])
def get_default():
    content = []
    if request.method == "GET":
      content = incomes_dft
    return jsonify(content)


@app.route('/delay',methods=["POST", "GET"])
def get_delay():
    content = []
    if request.method == "GET":
      content = incomes_dly
    return jsonify(content)

if __name__ == '__main__':
    app.run(port=5007)
