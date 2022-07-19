from cassandra.cqlengine import columns, connection
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table

class Profile(Model):
    id              = columns.Integer(primary_key=True)
    age             = columns.Integer(required=False)
    name            = columns.Text(required=True)
    email           = columns.Text(required=False)
    picture         = columns.Text(required=False)
    phone           = columns.Text(required=False)
    address         = columns.Text(required=False)
    preferences     = columns.List(columns.Text, default=[], required=False)

def init_db(db_settings):
	auth_provider = PlainTextAuthProvider(username=db_settings['userName'], password=db_settings['password'])
	connection.setup([db_settings['host']], "profile", protocol_version=4, port= db_settings['port'], auth_provider=auth_provider)
	sync_table(Profile)
