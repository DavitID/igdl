from flask import render_template, request, redirect, url_for, Flask
from igdl.main import Ingfo

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/", methods=["POST"])
def index_post():
  url = request.form["uri"]
  if not url:
    return redirect(url_for("index"))

  konten = Ingfo(url)
  return render_template("success.html", jadi = zip(konten.Source(),konten.Image()))

@app.route("/tentang")
def ttg():
  return render_template("info.html")

@app.route("/donasi")
def donate():
  return render_template("donasi.html")

@app.errorhandler(AttributeError)
def err_att(err):
  return render_template("err.html")

@app.errorhandler(404)
def not_found(nfn):
  return render_template("nfound.html")

if __name__ == "__main__":
  app.run(debug = True)
