from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

x0=0
y0=0
x1=500
y1=100
draw_line( x0, y0, x1, y1, screen, color )

display(screen)
save_extension(screen, 'img.png')