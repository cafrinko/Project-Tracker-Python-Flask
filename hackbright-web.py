from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','0')
    first, last, github = hackbright.get_student_by_github(github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student"""

    first_name = request.form.get('first')
    last_name = request.form.get('last')
    github = request.form.get('github')
    
    hackbright.make_new_student(first_name, last_name, github)

    html = render_template("new_student_info.html",
                            first=first_name,
                            last=last_name,
                            github=github)

    return html

@app.route("/student-form-display")
def new_student_form():
    """Displays empty student form"""

    return render_template("new_student.html")

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
