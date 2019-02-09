from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

'''
x0=0
y0=0
x1=234
y1=3232
draw_line( x0, y0, 500, 200, screen, color )
draw_line( x0, y0, x1, y1, screen, color )
draw_line( x0, y0, 500, 500, screen, color )
draw_line( 0, 400, 1000, y0, screen, color )
draw_line( 100, 100, 1000, y0, screen, color )
draw_line( 0, 100, 1000, 100, screen, color )
draw_line( 100, 0, 100, 1000, screen, color )
'''


x0=100
y0=100
x1=400
y1=400
green=255
blue=100
while x0<400:
    color = [ 0,green,blue ]
    draw_line( x0, y0, x1, y1, screen, color )
    x0+=5
    x1-=5
    if green>100:
        green-=0.5
    if blue<255:
        blue+=1

        
red=255
x2=0
y2=0
x3=50

x4=500
y4=500
x5=450

while y2<500:   
    color = [ red,0,0 ]
    draw_line( x2, y2, x3, y2, screen, color )
    draw_line( x4, y4, x5, y4, screen, color )
    if red>100:
        red-=0.5
    y2+=2
    y4-=2
    
display(screen)
save_extension(screen, 'img.png')
