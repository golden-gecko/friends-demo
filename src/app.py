from connexion import FlaskApp

app = FlaskApp(__name__)
app.add_api('v1.yaml')

flask_app = connexion_app.app
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
    os.environ.get('POSTGRES_USER'), os.environ.get('POSTGRES_PASSWORD'),
    os.environ.get('POSTGRES_HOST'), os.environ.get('POSTGRES_DATABASE_NAME')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
