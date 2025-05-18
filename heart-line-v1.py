import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

setup(width=380, height=400)
speed(0)
bgcolor("black")

color("#f73487")

# Draw the heart shape
penup()
goto(0, -200)  # Start below the center to fit the heart well
pendown()

begin_fill()
for i in range(628):  # A complete heart shape
    x = hearta(i / 100) * 10
    y = heartb(i / 100) * 10
    goto(x, y)
   
end_fill()

# Write text below the heart
penup()
goto(0, -250)  # Position below the heart
pendown()
color("white")
write("جمعه مباركه", align="center", font=("Arial", 24, "bold"))

hideturtle()
done()
