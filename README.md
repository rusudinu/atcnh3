# Init docker swarm 
```bash
docker swarm init
```

# Build the image
```bash
docker build -t whoami-app:latest .
```

# Deploy the stack
```bash
docker stack deploy -c docker-compose.yml whoami-stack
```

# List all services in the stack
```bash
docker stack services whoami-stack
```

# Check running containers
```bash
docker stack ps whoami-stack
```

# View service logs
```bash
docker service logs whoami-stack_whoami-service
```

# Scale the service (if you want to change the number of replicas)
```bash
docker service scale whoami-stack_whoami-service=5
```

# Remove the stack when needed
```bash
docker stack rm whoami-stack
```

