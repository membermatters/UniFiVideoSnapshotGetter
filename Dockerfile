# Specify our base image
FROM python:3.8.10
MAINTAINER Jaimyn Mayer (infrastructure@hsbne.org)

# Copy our requirements across and install dependencies
# Splitting this and copying the full code means we take advantage of the docker cache layers and don't have to
# reinstall everything when the code changes
RUN mkdir /usr/app && mkdir /usr/app/config && mkdir /usr/app/output && mkdir /usr/app/src
ADD ./requirements.txt /usr/app/src
WORKDIR /usr/app/src
RUN pip install --no-cache-dir -r requirements.txt

# Add the rest of our code
ADD . /usr/app/src
VOLUME /user/app/config
VOLUME /user/app/output

# Run the app
CMD ["python", "snapshotgetter.py"]