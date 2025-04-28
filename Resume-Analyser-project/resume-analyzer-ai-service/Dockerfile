# Use Python 3.12 as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the entire current directory into the container's /app directory
COPY . .

# Download the wait-for-it.sh script (if not already in the directory)
RUN curl -o /app/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && chmod +x /app/wait-for-it.sh

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Download the spacy model en_core_web_sm
RUN python -m spacy download en_core_web_sm

# Expose port 5000
EXPOSE 5000

# Set the entry point to wait for MySQL to be ready and then start the app
CMD ["/app/wait-for-it.sh", "resumeanalyser-db:3306", "--", "python3", "app.py"]
