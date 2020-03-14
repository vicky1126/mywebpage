import glob
import os
from flask import Flask, render_template
server = Flask("Vicky")

@server.route("/")
def index():
    ds = glob.glob("diary/*")
    ds = [d.split("/")[-1] for d in ds]
    return render_template("index.html", dirs = ds)

@server.route("/diary/<c>")
def diary(c):
    fs = glob.glob("diary/" + c +"/*.txt")
    contents = []
    for i, fn in enumerate(fs):
        name = os.path.split(fn)[-1].replace(".txt","")
        f = open(fn)
        diary = f.read()
        f.close()
        contents.append((name, diary, i))

    return render_template("diary.html", cs = contents)

