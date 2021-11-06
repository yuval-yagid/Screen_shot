FROM selenium/standalone-chrome
MAINTAINER yuval yagid

# Install packages
RUN sudo apt-get update && \
    sudo apt-get install --no-install-recommends -y python3-pip apt-utils
WORKDIR /usr/src/app
# Install selenium & pyvirtualdisplay
RUN pip3 install selenium requests

# Copy python scripts
COPY SS.py SS.py

# Run script
ENTRYPOINT ["python3", "SS.py"]
