from flask import Flask,render_template

app = Flask(__name__)


goal_list = {"Plant Trees":[50000,29000,0,"images/donate1.jpg"],
             "Animal Healthcare":[50000,25000,0,"images/donate2.jpg"],
             "Water Drone Research":[50000,0,0,"images/donate3.jpg"],
             "Awareness Campaigns":[50000,12313,0,"images/donate4.jpg"], 
             }

@app.route("/")
def index():
    return render_template("index.html",goal_list=goal_list)


@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)