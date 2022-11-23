from flask import render_template,Flask,request
import pickle
import waitress

appl=Flask(name)
file=open("model.pkl","rb")
from waitress import serve
serve(appl, host="0.0.0.0", port=8080)

knn=pickle.load(file)
file.close()

@appl.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        myDict = request.form
        type1= myDict["elevation_ft"]
        pred = [type1]
        res=knn.predict([pred])[0]
        return render_template("result.html",elevation_ft=type1,res=res)
    return render_template("index.html")
    return 'OK'
if name == "main":
    appl.run(debug=True)