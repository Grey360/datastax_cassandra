from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import yaml


def connect_datastax(username, password, scb):
    cloud_config = { 'secure_connect_bundle': scb }
    auth_provider = PlainTextAuthProvider(username, password)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()

    row = session.execute("select release_version from system.local").one()
    if row:
        print(row[0])
    else:
        print("An error occurred.")

with open('config.yaml') as conf:
    yaml_content = yaml.load(conf, yaml.FullLoader)
    connect_datastax(
        yaml_content['username'],
        yaml_content['password'],
        yaml_content['secure-connect-bundle']
    )
    