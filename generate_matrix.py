import random

width = 900
height = 300
columns = 50
chars = "01"

svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">

<defs>
  <!-- Strong Neon Blue Glow -->
  <filter id="neonGlow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="4" result="blur"/>
    <feColorMatrix type="matrix"
      values="0 0 0 0 0
              0 0 0 0 0.8
              0 0 0 0 1
              0 0 0 1 0" />
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

</defs>

<rect width="100%" height="100%" fill="black"/>
'''

column_width = width // columns

for i in range(columns):
    x = i * column_width
    duration = random.uniform(3, 6)
    delay = random.uniform(0, 3)

    for j in range(6):  # fewer per column to avoid overlap
        y_start = random.randint(-height, 0)
        char = random.choice(chars)

        svg += f'''
        <text x="{x}"
              y="{y_start}"
              fill="#00aaff"
              font-size="18"
              font-family="monospace"
              filter="url(#neonGlow)">

            {char}

            <animate attributeName="y"
                     from="{y_start}"
                     to="{height+20}"
                     dur="{duration}s"
                     begin="{delay}s"
                     repeatCount="indefinite"/>

        </text>
        '''

svg += "</svg>"

with open("github-matrix.svg", "w") as f:
    f.write(svg)

print("Neon blue matrix generated.")
