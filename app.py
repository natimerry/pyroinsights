from flask import Flask, render_template, request
import itertools

app = Flask(__name__)


goal_list = {
    "Plant Trees": [50000, 0, 0, "images/donate1.jpg"],
    "Animal Healthcare": [50000, 0, 0, "images/donate2.jpg"],
    "Water Drone Research": [50000, 0, 0, "images/donate3.jpg"],
    "Awareness Campaigns": [50000, 0, 0, "images/donate4.jpg"],
}


donatee_list = [
    {
        "Sophia R.": [
            "Innovation for Progress",
            "What sets this organization apart is their innovation. They embrace technology, forge collaborations, and constantly seek fresh ways to better the world.",
        ]
    },
    {
        "Mark L.": [
            "Catalyzing Change",
            "The positive shifts brought about by this organization are palpable. They've revitalized communities, offered education, and become a force for meaningful change.",
        ],
    },
    {
        "Sarah W.": [
            "A Heartfelt Commitment to Charity",
            "Every contribution is a step towards genuine change. This organization's transparency and effectiveness reassure me that my support is truly making a difference.",
        ],
    },
]


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        donatee_list.append(
            {
                f"{request.form['firstname']} {request.form['lastname']}": [
                    request.form["title"],
                    request.form["message"],
                ]
            }
        )
        goal_list[request.form['goal']][1] += int(request.form['donate'])

    donatees_dict = {}
    for donatee in donatee_list[-3:]:
        name, value = list(donatee.items())[0]
        donatees_dict[name] = value

    return render_template("index.html", goal_list=goal_list, donatees=donatees_dict)


@app.route("/donate/", methods=["GET"])
def donate():
    if request.method == "GET":
        print(request.args.get('goal'))
    return render_template("donate.html",goal=request.args.get('goal'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
