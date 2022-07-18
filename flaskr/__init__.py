import os
from flask import Flask
import yaml
from yaml.loader import SafeLoader
from flaskr.profile_routes import add_profile_routes
from pathlib import Path
from .db import init_db

path = Path(__file__).parent.absolute()

with open(os.path.join(path,'config.yaml')) as f:
    data = yaml.load(f, Loader=SafeLoader)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
		APP_SETTINGS = data
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    init_db(app.config['APP_SETTINGS']['db'])
    add_profile_routes(app)

    return app
