import requests
import json
import time
import os

default_output = "/usr/app/output/"


def validate_config():
    if config.get("apiKey") and config.get("protocol") and config.get("port") and config.get("host") and config.get(
            "cameras") and config.get("frequency"):
        return True

    else:
        raise RuntimeError("Invalid configuration file")


def get_camera_url(camera_id):
    return config["protocol"] + f"://{config['host']}:{config['port']}/api/2.0/snapshot/camera/{camera_id}?force=true&apiKey={config['apiKey']}"


while True:
    with open('/usr/app/config/config.json') as json_file:
        config = json.load(json_file)

    validate_config()

    for camera in config["cameras"]:
        url = get_camera_url(camera["id"])

        r = requests.get(url)
        if r.status_code == 200:
            print("successfully got snapshot for " + camera["name"])
            open(os.path.join(default_output, camera["name"].replace(" ", "-")) + ".jpg", 'wb').write(r.content)

        else:
            print("Error grabbing snapshot for " + camera["name"])

    time.sleep(config["frequency"])
