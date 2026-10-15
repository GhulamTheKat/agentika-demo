from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Agentika 2.0 Agent API", description="Custom Agent deployed on Alternate Clouds")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Agentika 2.0 | Alternate Clouds</title>
            <style>
                body { 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    background-color: #0000AF; /* AF Dark Blue */
                    color: #F9F5EE; /* AF Cream */
                    text-align: center; 
                    padding-top: 10vh; 
                }
                h1 { 
                    color: #0BEBEA; /* AF Sky */
                    font-size: 3.5em; 
                    margin-bottom: 10px;
                }
                .container { 
                    background-color: #000AFF; /* AF Brand Blue */
                    padding: 40px 60px; 
                    border-radius: 12px; 
                    display: inline-block; 
                    box-shadow: 0 8px 32px rgba(0,0,0,0.5); 
                }
                a { 
                    color: #0000AF; 
                    background-color: #FFC7AA; /* AF Apricot */
                    padding: 10px 20px;
                    border-radius: 6px;
                    text-decoration: none; 
                    font-weight: bold; 
                    display: inline-block;
                    margin-top: 20px;
                    transition: 0.2s;
                }
                a:hover { 
                    transform: scale(1.05);
                }
                .tag {
                    font-size: 0.9em;
                    color: #A5B2FF; /* AF Medium Blue */
                    letter-spacing: 2px;
                    text-transform: uppercase;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="tag">NaSCon 2026 x Grayhat</div>
                <h1>🚀 Agentika 2.0 Deployment Successful!</h1>
                <p>Your custom Python Agent is now routing live traffic on <b>Alternate Clouds</b>.</p>
                <a href="/docs">View Interactive API Dashboard</a>
            </div>
        </body>
    </html>
    """

@app.get("/agent/status")
def status():
    return {"status": "online", "model": "ready", "provider": "Alternate Clouds Edge"}
