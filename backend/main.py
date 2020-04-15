import flask

app = flask.Flask(__name__)


@app.route("/")
def serve_index():
    return flask.render_template("index.html", token="kiscica")


# mandatory Hello World until i figure out how to render more pages in the templates folder beside index.html
@app.route("/home")
def serve_help():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)

