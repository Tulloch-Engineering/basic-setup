# Use the official Node.js LTS image as the base image
FROM node:lts

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the current directory to the working directory inside the container
COPY package*.json ./

RUN npm install

COPY . .

ENV PORT=8000

# Expose port 8000
EXPOSE 8000

CMD ["npm", "run", "dev"]
