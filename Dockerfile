
# Use an official Python runtime as a parent image
FROM garagon/ipopt:V0.2

# Set the working directory to usr/src/app
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy the current directory contents into the container usr/src/app
COPY requirements.txt /usr/src/app/

# #new addition
RUN apt-get autoclean
RUN apt-get clean

RUN apt-get update -y && apt-get install -y \
	gcc build-essential gfortran libatlas-base-dev gfortran libblas-dev liblapack-dev libatlas-base-dev wget libpng-dev python3-pip python3-dev

RUN pip3 install --upgrade pip

RUN pip3 install -U requests
RUN pip3 install -U pyomo
RUN pip3 install -U gunicorn
RUN pip3 install -U sh
RUN pip3 install -U Pyro4
RUN pip3 install -U connexion
RUN pip3 install -U paho-mqtt
RUN pip3 install -U pyzmq
RUN pip3 install -U psutil
RUN apt-get update -y && apt-get install -y \
    libhdf5-serial-dev libatlas-dev python3-setuptools


#RUN pip3 install setuptools
#RUN apt-get install libhdf5-serial-dev
RUN pip3 install -U numpy==1.14.3
RUN pip3 install -U h5py
RUN pip3 install -U scipy
RUN pip3 install -U pandas==0.22.0
RUN pip3 install -U sklearn
RUN pip3 install -U tensorflow==1.8.0
RUN pip3 install -U keras==2.1.6
RUN pip3 install -U senml
RUN pip3 install -U redis

#COPY myAgent /usr/src/app/myAgent

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Install the gpio library for Raspberry pi
#RUN pip install rpi.gpio
#RUN pip3 install --upgrade pip
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip3 install -r requirements.txt
#RUN pyomo install-extras
#COPY ofw.py /usr/src/app/
#COPY optimization /usr/src/app/optimization
#COPY utils /usr/src/app/utils
#COPY prediction /usr/src/app/prediction
#COPY swagger_server /usr/src/app/swagger_server
#COPY IO /usr/src/app/IO
#VOLUME /usr/src/app/optimization
#ENTRYPOINT ["python3", "prediction/training/pyroAdapter.py"]
#ENTRYPOINT ["python3", "webServices/webcontroller.py"]

WORKDIR /usr/src/app

COPY ofw.py /usr/src/app/
COPY optimization /usr/src/app/optimization
COPY utils /usr/src/app/utils
COPY prediction /usr/src/app/prediction
COPY swagger_server /usr/src/app/swagger_server
COPY IO /usr/src/app/IO
COPY mock_data /usr/src/app/mock_data


