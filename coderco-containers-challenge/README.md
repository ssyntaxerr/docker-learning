# Containers Challenge 📦

In this challenge, I built and containerized a simple multi-container application using Docker and Docker Compose. The goal was to run a Flask web application alongside a Redis database, with both services isolated, configurable, and managed together using Docker Compose.

The focus of this project is on demonstrating containerization, service communication, persistence, and orchestration rather than the internal logic of the Python application itself.

## Architecture

The application is composed of two services:

#### Web Service (Flask)
A Python Flask application running inside its own Docker container.

#### Redis Service
A Redis key-value store running in a separate container and used by the Flask application to persist data.

Both services are defined in a single docker-compose.yml file, allowing them to be built, networked, and run together with one command.

### Dockerization Strategy

#### Flask Application Container
The Flask application is containerized using a custom Dockerfile that:
Uses a lightweight Python base image
Installs dependencies from a requirements.txt file
Exposes port 5000 for HTTP traffic
Runs the application inside the container
Uses a non-root user for improved security
This ensures the application runs in a consistent, portable, and secure environment.

#### Redis Container
Redis is also containerized using its own Dockerfile, as required by the challenge.
The Dockerfile extends the official Redis image, keeping the setup minimal while satisfying the requirement to create a custom Redis Dockerfile.
The Redis service is not exposed to the host machine and is only accessible internally by the Flask service.

#### Docker Compose Orchestration
Docker Compose is used to manage the full application stack.
Using Docker Compose, I was able to:
Automatically build both the Flask and Redis images
Define service-to-service communication using Docker’s internal DNS
Pass Redis connection details to the Flask service via environment variables
Control service startup order using dependencies
The entire application can be started with:

docker compose up --build

#### Persistent Storage
To ensure Redis data persists across container restarts, a named Docker volume is used and mounted to Redis’s data directory. This allows the visit count stored in Redis to survive container shutdowns and rebuilds.

#### Scaling the Application
As a bonus, Docker Compose’s built-in scaling feature is used to run multiple instances of the Flask service:

docker compose up --scale web=3

Docker automatically load-balances incoming requests across the running Flask containers, while all instances share the same Redis backend.


## Final thoughts 📃

Having little to no knowledge about Python and redis made it a little difficult for me to complete this challenge. But, after some reasearch and getting help when necessary, I think I've grasped what it means to containerize. 

When I containerize an application, I’m choosing to package my work in a way that removes uncertainty. I’m no longer relying on assumptions about what’s installed on a machine or how something should be configured, everything the application needs lives alongside it. That gives me confidence that if it runs for me, it will run the same way anywhere else.

Containerization also changes how I think about systems. Instead of one environment doing everything, each responsibility gets its own space. The application focuses on serving requests, Redis focuses on data, and Docker handles how they talk to each other. That separation makes the whole setup easier to reason about, easier to debug, and easier to scale.

Most importantly, containerizing forces me to be intentional. I have to define how the application starts, what it depends on, and how it’s exposed. There’s no hidden setup or manual steps — the environment becomes part of the codebase. That shift is what makes the project feel production-ready rather than “it works on my machine.”
