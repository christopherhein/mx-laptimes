from flask import Flask
import yaml
import json

app = Flask(__name__)

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

def create_hal_object(id, object):
    halified = {
            'id': id,
            "_links": {
                "self": { "href": "/laptimes/"+id },
                "tracks": { "href": "/tracks/"+id }
                }
            }
    return merge_two_dicts(halified, object)

@app.route("/laptimes/<id>")
def laptimes(id):
    config = yaml.load(open('laptimes.yml'))
    return json.dumps(create_hal_object(str(id), config['laptimes'][str(id)]))

app.run(host='0.0.0.0')

