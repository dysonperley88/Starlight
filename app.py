from flask import Flask, request, Response, send_from_directory

app = Flask(__name__)

@app.route("/kctv2/xml/gb_config_<string:lang>.xml")
def configxml(lang):
    return send_from_directory("conf","gb_config_"+lang+".xml")

@app.route("/kctv2/<string:lang>/kirby<string:vidN>.mo")
def servevideo(lang,vidN):
    return send_from_directory(lang,"kirby"+vidN+".mo")

@app.route("/kctv2/video/promo<string:promoN>.mo")
def promos(promoN):
    return send_from_directory("video","promo"+promoN+".mo")