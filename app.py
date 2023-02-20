from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id" : 1,
    "title" : "Data Analyst",
    "location": "New York",
    "salary": "$160,000"
  },
  {
    "id" : 2,
    "title" : "Data Scientist",
    "location": "San Fransisco",
    "salary": "$230,000"
  },
  {
    "id" : 3,
    "title" : "Frontend Engineer",
    "location": "Mumbai",
    "salary": "₹15,00,000"
  },
  {
    "id" : 4,
    "title" : "Software Developer",
    "location": "Banglore",
    "salary": "₹23,00,000"
  },
  {
    "id" : 5,
    "title" : "Data Research Engineer",
    "location": "Remote",
    "salary": "$160,000"
  },
]

@app.route("/")
def index():
  return render_template("home.html", title="Jovian", jobs=JOBS)

@app.route("/api/jobs")
def jobs_json():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)