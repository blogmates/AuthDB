# Use the official PostgreSQL image from the Docker Hub
FROM postgres:latest

# Set environment variables (optional)
ENV POSTGRES_DB=authDB
ENV POSTGRES_HOST_AUTH_METHOD=trust
# Copy initialization script into the container


WORKDIR scripts

COPY ./scripts /scripts

# CMD ["python3", "init.py"]
