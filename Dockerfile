# set base image (host OS)
FROM python:latest

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requierments.txt .

# install dependencies
RUN pip install -r requierments.txt

# copy the content of the local src directory to the working directory
COPY ./ .

# set the token for the telegram bot
ENV TOKEN="6645809775:AAEUDxtb2_jxSJ-BuDwLzrcNRiLbwsg_yOw"

# command to run on container start
CMD [ "python", "./main.py" ]