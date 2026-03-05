import random

width = 900
height = 300
columns = 40
chars = "01"

svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">

<defs>
  <!-- Neon Glow Filter -->
  <filter id="neonGlow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="3" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <!-- Color Shift Animation -->
  <linearGradient id="colorShift" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#9d00ff">
      <animate attributeName="stop-color"
               values="#9d00ff;#ff00ff;#9d00ff"
               dur="4s"
               repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" stop-color="#4b0082">
      <animate attributeName="stop-color"
               values="#4b0082;#9d00ff;#4b0082"
               dur="4s"
               repeatCount="indefinite"/>
    </stop>
  </linearGradient>

</defs>

<rect width="100%" height="100%" fill="black"/>
'''

column_width = width // columns

for i in range(columns):
    x = i * column_width
    duration = random.uniform(3, 6)
    delay = random.uniform(0, 3)

    for j in range(8):
        y_start = random.randint(-300, 0)
        char = random.choice(chars)

        svg += f'''
        <text x="{x}" y="{y_start}"
              fill="url(#colorShift)"
              font-size="16"
              filter="url(#neonGlow)"
              opacity="0.8">
            
            {char}

            <!-- Falling Animation -->
            <animate attributeName="y"
                     from="{y_start}"
                     to="{height+20}"
                     dur="{duration}s"
                     begin="{delay}s"
                     repeatCount="indefinite"/>

            <!-- Pulsing Effect -->
            <animate attributeName="opacity"
                     values="0.3;1;0.3"
                     dur="2s"
                     repeatCount="indefinite"/>

        </text>
        '''

svg += "</svg>"

with open("matrix.svg", "w") as f:
    f.write(svg)

print("Cyberpunk neon matrix generated.")
