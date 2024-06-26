# Base image
FROM node:21

WORKDIR /app

# Install dependencies
COPY package.json /app/package.json
RUN npm install

# Copy app files
COPY . /app

# Start the app
CMD ["npm", "build"]
