FROM node:18-alpine

WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy application code
COPY . .

# Build the application
RUN npm run build

# Install serve to serve the built files
RUN npm install -g serve

# Expose port
EXPOSE 5173

# Serve the app
CMD ["serve", "-s", "dist", "-l", "5173"]
