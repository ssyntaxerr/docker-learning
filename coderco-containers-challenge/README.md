# Containers Challenge

In this challenge, I built and containerized a simple multi-container application using Docker and Docker Compose. The goal was to run a Flask web application alongside a Redis database, with both services isolated, configurable, and managed together using Docker Compose.

The focus of this project is on demonstrating containerization, service communication, persistence, and orchestration rather than the internal logic of the Python application itself.

Architecture

The application is composed of two services:

Web Service (Flask)
A Python Flask application running inside its own Docker container.

Redis Service
A Redis key-value store running in a separate container and used by the Flask application to persist data.

Both services are defined in a single docker-compose.yml file, allowing them to be built, networked, and run together with one command.

Dockerization Strategy
Flask Application Container

The Flask application is containerized using a custom Dockerfile that:

Uses a lightweight Python base image

Installs dependencies from a requirements.txt file

Exposes port 5000 for HTTP traffic

Runs the application inside the container

Uses a non-root user for improved security

This ensures the application runs in a consistent, portable, and secure environment.

Redis Container

Redis is also containerized using its own Dockerfile, as required by the challenge.
The Dockerfile extends the official Redis image, keeping the setup minimal while satisfying the requirement to create a custom Redis Dockerfile.

The Redis service is not exposed to the host machine and is only accessible internally by the Flask service.

Docker Compose Orchestration

Docker Compose is used to manage the full application stack.

Using Docker Compose, I was able to:

Automatically build both the Flask and Redis images

Define service-to-service communication using Docker’s internal DNS

Pass Redis connection details to the Flask service via environment variables

Control service startup order using dependencies

The entire application can be started with:

docker compose up --build

Persistent Storage

To ensure Redis data persists across container restarts, a named Docker volume is used and mounted to Redis’s data directory. This allows the visit count stored in Redis to survive container shutdowns and rebuilds.

Scaling the Application

As a bonus, Docker Compose’s built-in scaling feature is used to run multiple instances of the Flask service:

docker compose up --scale web=3


Docker automatically load-balances incoming requests across the running Flask containers, while all instances share the same Redis backend.
