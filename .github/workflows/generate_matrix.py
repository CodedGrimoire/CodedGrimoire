import requests
import datetime

USERNAME = "CodedGrimoire"

# Get contribution data from GitHub API
url = f"https://api.github.com/users/{USERNAME}/events"
response = requests.get(url)
events = response.json()

# Simple animation-style SVG
width = 900
height = 200

svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<style>
@keyframes glow {{
  0% {{ opacity: 0.3; }}
  50% {{ opacity: 1; }}
  100% {{ opacity: 0.3; }}
}}
.matrix {{
  fill: #00ff00;
  font-family: monospace;
  font-size: 14px;
  animation: glow 2s infinite;
}}
</style>

<rect width="100%" height="100%" fill="black"/>
<text x="20" y="40" class="matrix">
Cyberpunk Contribution Stream
</text>
</svg>
'''

with open("matrix.svg", "w") as f:
    f.write(svg)

print("Matrix SVG generated.")
