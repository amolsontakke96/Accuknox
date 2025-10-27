# Use a lightweight Ubuntu base image
FROM ubuntu:22.04

# Set noninteractive mode for apt
ENV DEBIAN_FRONTEND=noninteractive

ENV PATH="/usr/games:${PATH}"

# Install dependencies
RUN apt update && \
    apt install -y fortune-mod cowsay netcat-openbsd && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your wisecow.sh script into the container
COPY wisecow.sh .

# Make it executable
RUN chmod +x wisecow.sh

# Expose port 4499
EXPOSE 4499

# Run the script
CMD ["./wisecow.sh"]
