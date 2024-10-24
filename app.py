from flask import Flask, render_template, request

import salary

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello() :
    sal = None
    if request.method == "POST":
        yoe = float(request.form["years_of_experience"])
        sal = salary.salary_prediction(yoe)
    return render_template("index.html", my_sal = sal)


if __name__ == "__main__":
    app.run(debug=True)