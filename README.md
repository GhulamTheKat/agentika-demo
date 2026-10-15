# Agentika 2.0 - Custom Agent Demo 🚀

A minimal, 3-file FastAPI boilerplate demonstrating how to deploy custom Python code on **Alternate Clouds** for the NaSCon Agentika Hackathon.

## What's in this Repository?
This repository contains the absolute minimum required to get a Python web server containerized and running:

* `main.py`: The Python application code (a simple FastAPI server).
* `requirements.txt`: The Python dependencies needed to run the code.
* `Dockerfile`: The blueprint that tells Alternate Clouds how to build the environment and expose the correct port.

## Deployment Instructions
To deploy this custom agent to Alternate Clouds:

1. **Fork** this repository to your own GitHub account.
2. Log in to your [Alternate Clouds Dashboard](https://clouds.alternatefutures.ai).
3. Click **Add Service** -> **GitHub Repo** and authorize your GitHub account.
4. Select your forked repository.
5. **Crucial:** Ensure the deployment port is set to `8000` (as defined in the Dockerfile).
6. Click Deploy!

*Built for the NaSCon 2026 Agentika 2.0 Hackathon.*
