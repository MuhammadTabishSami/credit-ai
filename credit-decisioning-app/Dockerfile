# # Use the official Node.js image from the Docker Hub
# FROM node:18

# # Set the working directory in the container
# WORKDIR /usr/src/app

# # Copy package.json and package-lock.json into the container
# COPY package*.json ./

# # Install dependencies
# RUN npm install

# # Copy the rest of the application code into the container
# COPY . .

# # Build the React application
# RUN npm run build

# # Install a simple HTTP server to serve the built files
# RUN npm install -g serve

# # Expose the port that the React app will run on
# EXPOSE 3000

# # Command to run the React application
# CMD ["serve", "-s", "build", "-l", "3000"]

# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Expose the port on which the app will run
EXPOSE 3000

# Serve the React app
CMD ["npx", "serve", "-s", "build", "-l", "3000"]

