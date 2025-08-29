# Base image: Use a slim Python variant for minimal footprint, matching the script's Python 3.x compatibility.
# This provides the interpreter and pip without extraneous OS packages.
FROM python:3.12-slim

# Set the working directory inside the container to /app.
# This organizes files and sets the context for relative paths.
WORKDIR /app

# Copy all files from the current directory (repo root) into /app.
# This includes the script; use .dockerignore to exclude unnecessary files like __pycache__.
COPY . /app

# Install dependencies: Streamlit is required for the web interface.
# --no-cache-dir avoids storing pip cache, keeping the layer small.
RUN pip install --no-cache-dir streamlit

# Expose the default Streamlit port for web access.
EXPOSE 8501

# Define the command to run when the container starts.
# This launches Streamlit in server mode; replace 'ecommerce_ai_agent.py' with your script name if different.
# --server.port specifies the port, --server.address binds to all interfaces for external access.
CMD ["streamlit", "run", "ecommerce_ai_agent.py", "--server.port=8501", "--server.address=0.0.0.0"]