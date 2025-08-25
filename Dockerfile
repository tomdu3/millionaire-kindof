FROM node:18

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies including Python
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Copy package files
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy Python requirements
COPY requirements.txt ./

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Your application's startup command
CMD ["npm", "start"]