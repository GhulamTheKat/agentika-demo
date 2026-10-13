# Agentika 2.0 Demo Agent

A lightweight Python (FastAPI) boilerplate agent designed for testing and deploying applications on **Alternate Clouds** during the **NaSCon Agentika 2.0 Hackathon**.

## Stack
* **Framework:** FastAPI
* **Runtime:** Python 3.10+
* **Deployment Target:** Alternate Clouds (`acc`)


## Quickstart / Local Testing
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/agentika-demo.git](https://github.com/your-username/agentika-demo.git)
   cd agentika-demo

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run locally:
   ```bash
   uvicorn main:app --reload --port 8000


## Deploying to Alternate Clouds
Deploy this repository directly using the Alternate Clouds CLI:
   ```bash
   acc services create --kind github --repo your-username/agentika-demo --port 8000
