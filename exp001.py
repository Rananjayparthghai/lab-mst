from flask import Flask

app = Flask(name)

@app.route('/')
def hello():
    return '\n\n\t\tKrish Jindal | 21BCS7871'

if name == 'main':
    app.run(debug=True)
