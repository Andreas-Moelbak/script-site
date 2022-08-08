import os
import subprocess
from flask import Flask, send_file, request, render_template, after_this_request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        first_name = str(request.form.get("fname"))
        last_name = str(request.form.get("lname"))
        file_path = "test.txt"

        subprocess.run(["python3",  "script.py", "-f", first_name, "-l", last_name, "-o", file_path])

        @after_this_request
        def remove_file(response):
            os.remove(file_path)
            return response

        return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
