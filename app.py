from flask import Flask, render_template
import itertools
app = Flask(__name__)


goal_list = {
    "Plant Trees": [50000, 29000, 0, "images/donate1.jpg"],
    "Animal Healthcare": [50000, 25000, 0, "images/donate2.jpg"],
    "Water Drone Research": [50000, 0, 0, "images/donate3.jpg"],
    "Awareness Campaigns": [50000, 12313, 0, "images/donate4.jpg"],
}


donatees = {
    "Sarah W.": [
        "A Heartfelt Commitment to Charity",
        "Every contribution is a step towards genuine change. This organization's transparency and effectiveness reassure me that my support is truly making a difference.",
    ]
,
    "Mark L.": [
        "Catalyzing Change",
        "The positive shifts brought about by this organization are palpable. They've revitalized communities, offered education, and become a force for meaningful change."
    ]
,
    "Sophia R.": [
        "Innovation for Progress",
        "What sets this organization apart is their innovation. They embrace technology, forge collaborations, and constantly seek fresh ways to better the world."
    ]
}


@app.route("/")
def index():
    out = dict(itertools.islice(donatees.items(), 3))

    return render_template("index.html", goal_list=goal_list,donatees=out)


@app.route("/about/")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
