# Start your image with a node base image
FROM node:18-alpine

# The /app directory should act as the main application directory
WORKDIR /django

# Copy the app package and package-lock.json file
COPY package*.json ./

# Copy local directories to the current local directory of our docker image (/app)
COPY requirements.txt  requirements.txt

# Install node packages, install serve, build the app, and remove dependencies at the end
RUN 
    pip3 intall -r requirements.txt
    npm install \
    && npm install -g serve \
    && npm run build \
    && rm -fr node_modules

EXPOSE 3000

# Start the app using serve command
CMD python manage.py runserver 127.0.0.1:8000