# Use the Alpine Linux base image
FROM alpine:latest

# Install necessary dependencies
RUN apk update && \
    apk add --no-cache \
    curl \
    python3 \
    py3-pip \
    groff \
    less \
    && pip3 install --upgrade awscli

# Install Node.js v19.1 using official Alpine packages
RUN apk add --no-cache nodejs npm

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY ./frontend/package.json ./frontend/package-lock.json /app/

# Install project dependencies
RUN npm install

# Copy the rest of the frontend files
COPY ./frontend /app

# Set the default command
CMD [ "node" ]
