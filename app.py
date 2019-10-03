from flask import Flask
from flask import render_template, request, jsonify, send_file, make_response
from kb import getkb

app = Flask(__name__)


@app.route('/')
def m():
    return render_template("index.html")


@app.route("/kb")
def kb():
    return render_template("kb.html")


@app.route("/api", methods=['POST'])
def api():
    try:
        username = int(request.form['username'])
        pwd = request.form['password']
        r = getkb(username, pwd)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"status": "500"})

    if "cookies" in r.keys():
        cookies = r.pop("cookies")
    else:
        cookies = {}
    rst = make_response(jsonify(r))
    for k in cookies.keys():
        rst.set_cookie(k, cookies[k])
    return rst


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5555, debug=True)