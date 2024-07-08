FROM python:3.9

# Install Chrome and Chromium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable chromium \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN chmod +x start.sh
# Copy only the 'myproject' folder
COPY mycountdown/ ./mycountdown/
COPY mycountdown/.env .
COPY start.sh .
# Add this line before the CMD instruction
EXPOSE 8000
# Run the application
CMD ["./start.sh"]