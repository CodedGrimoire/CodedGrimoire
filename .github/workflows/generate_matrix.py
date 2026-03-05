import random

width = 900
height = 300
columns = 30

chars = "01"

svg_header = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="black"/>
'''

svg_content = ""

for i in range(columns):
    x = i * (width // columns)
    delay = random.uniform(0, 5)
    duration = random.uniform(3, 6)

    svg_content += f'''
    <text x="{x}" y="-20" fill="#00ff00" font-size="14">
        {random.choice(chars)}
        <animate attributeName="y"
                 from="-20"
                 to="{height+20}"
                 dur="{duration}s"
                 begin="{delay}s"
                 repeatCount="indefinite"/>
    </text>
    '''

svg_footer = "</svg>"

with open("matrix.svg", "w") as f:
    f.write(svg_header + svg_content + svg_footer)

print("Real Matrix rain generated.")
