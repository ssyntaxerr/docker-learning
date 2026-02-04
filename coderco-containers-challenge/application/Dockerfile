FROM python:3.11-slim

# Create a non-root user
RUN useradd -m appuser

# Set working directory
WORKDIR /app

# Copy dependencies
COPY application/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY application/app.py .

# Give ownership of the app directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Document that the Flask app listens on port 5000
EXPOSE 5000

# Start the Flask application when the container runs
CMD [ "python", "app.py" ]