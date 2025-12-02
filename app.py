from flask import Flask
from blueprints.main import main as main_blueprint
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(main_blueprint)

@app.context_processor
def inject_globals():
    return {'current_year': datetime.now().year}

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run(debug=True)