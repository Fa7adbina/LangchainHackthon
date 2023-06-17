from legal import Legal_Researcher
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route('/backend', methods=['POST'])
def backend():
    # Receive the user input and language from the frontend
    user_input = request.json['message']
    language = request.json['language']

    # Process the user input and language using your Python function
    response = Legal_Researcher(user_input, language)

    # Return the response to the frontend
    return jsonify({'message': response})


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)