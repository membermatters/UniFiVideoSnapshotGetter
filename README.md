# UniFi Video Snapshot Getter
This docker container will grab a configuration file with a list of cameras in it and grab a snapshot from a Ubiquiti 
NVR every x seconds. See below to get started.

## Quick start
1) Make sure Docker is available on your system.
2) Make two separate directories for your config and output images and copy your config file to the config one.
3) Run `docker pull hsbne/unifi-video-snapshot-getter` to download the image.
4) Run the following to start the container:
```
docker run --name unifi-video-snapshot-getter -v /path/to/config/directory:/usr/app/config -v /path/to/output/directory:/usr/app/output --restart always hsbne/unifi-video-snapshot-getter
```

Note: you must create the config & output directories, and a config file before starting the container.

Tip: you should end up with something like this before starting the container:
```
/home/user/snapshotgetter/config/
/home/user/snapshotgetter/config/config.json
/home/user/snapshotgetter/output/
``` 

## Using the output files
You'll find all of the jpg snapshots in the output folder you specified. They will be in the format <camer-name.jpg> and all spaces from the camera name will be replaced with a "-" for convenience in serving it on the web. ie "Test Camera" will output as "Test-Camera.jpg". 
