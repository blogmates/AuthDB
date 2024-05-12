# Use the official PostgreSQL image from the Docker Hub
FROM postgres:latest

# Set environment variables (optional)
ENV POSTGRES_DB=authDB
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_HOST_AUTH_METHOD=trust
# Copy initialization script into the container

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-psycopg2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR scripts

COPY ./scripts /scripts

EXPOSE 5432

# Update shebang line in init.py
RUN sed -i 's/\/usr\/bin\/env python3/\/usr\/bin\/python3/' /scripts/init.py

CMD ["python3", "init.py"]
