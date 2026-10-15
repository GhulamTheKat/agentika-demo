from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI(title="Agentika Idea Generator")

# A list of fun/snarky project ideas tailored for CS students
IDEAS = [
    "A brutally honest AI code reviewer that roasts your GitHub commits.",
    "An AI agent that automatically cancels your subscription free trials before they charge you.",
    "A Discord bot that summarizes 500 unread messages into a 3-bullet haiku.",
    "An AI negotiator that haggles on Facebook Marketplace for you.",
    "A voice agent that pretends to be a dial-up modem to annoy telemarketers.",
    "An AI study buddy that locks your laptop if you open TikTok."
]

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Agentika 2.0 | Idea Generator</title>
        <style>
            body {
                background-color: #000010;
                color: #0BEBEA;
                font-family: 'Courier New', Courier, monospace;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .terminal {
                background: #0000AF; /* AF Dark Blue */
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 20px #0BEBEA; /* AF Sky Glow */
                text-align: center;
                max-width: 600px;
            }
            h1 { color: #F9F5EE; /* AF Cream */ margin-bottom: 5px; }
            p { font-size: 1.1em; color: #FFC7AA; /* AF Apricot */ margin-top: 0; }
            button {
                background: #0BEBEA;
                color: #0000AF;
                border: none;
                padding: 15px 30px;
                font-size: 1.2em;
                font-weight: bold;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 20px;
                transition: transform 0.1s, box-shadow 0.1s;
            }
            button:active { 
                transform: scale(0.95); 
            }
            button:hover {
                box-shadow: 0 0 15px #0BEBEA;
            }
            #idea-box {
                margin-top: 30px;
                padding: 20px;
                border: 2px dashed #0BEBEA;
                border-radius: 5px;
                background: rgba(0,0,0,0.3);
                min-height: 80px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.2em;
                line-height: 1.4;
            }
            .tag {
                font-size: 0.8em;
                color: #A5B2FF;
                letter-spacing: 2px;
                text-transform: uppercase;
                margin-bottom: 15px;
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="terminal">
            <span class="tag">NaSCon 2026 x Grayhat</span>
            <h1>🤖 Agentika Terminal</h1>
            <p>Status: ONLINE | Hosted on Alternate Clouds</p>
            
            <button onclick="getIdea()">Generate Project Idea</button>
            
            <div id="idea-box">Click the button to ping the FastAPI backend...</div>
        </div>

        <script>
            // This JavaScript talks to your Python backend!
            async function getIdea() {
                const box = document.getElementById('idea-box');
                box.innerHTML = "<em>Pinging Alternate Clouds edge server...</em>";
                
                // Add a tiny artificial delay so it feels like it's "thinking"
                setTimeout(async () => {
                    const response = await fetch('/generate-idea');
                    const data = await response.json();
                    box.innerHTML = "<strong>" + data.idea + "</strong>";
                }, 400);
            }
        </script>
    </body>
    </html>
    """

@app.get("/generate-idea")
def generate_idea():
    # The frontend calls this endpoint to get a random idea
    idea = random.choice(IDEAS)
    return {"idea": idea}
