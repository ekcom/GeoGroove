# Base image
FROM node:21

WORKDIR /frontend

# Install dependencies
COPY package.json /frontend/package.json
RUN npm install

# Copy app files
COPY . /frontend

# Start the app
RUN npm run build
