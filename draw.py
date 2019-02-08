from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=y1-y0
    B=-1*(x1-x0)
    
    if (x1-x0)==0:
        while (y<=y1):
            plot(screen,color,x,y)
            y+=1
        
    if (x1-x0)!=0:
        m=(y1-y0)/(x1-x0)
        
        if m>=0 and m<1:
            d=2*A+B
            while (x<=x1):
                plot(screen,color,x,y)
                if (d>0):
                    y+=1
                    d+=2*B
                x+=1
                d+=2*A
            
        if m>=1:
            d=A+2*B
            while (y<=y1):
                plot(screen,color,x,y)
                if (d<0):
                    x+=1
                    d+=2*A
                y+=1
                d+=2*B
            
        if m<0 and m>-1:
            d=2*A+B
            while (x<=x1):
                plot(screen,color,x,y)
                if (d<0):
                    y-=1
                    d-=2*B
                x+=1
                d+=2*A
        if m<=-1:
            d=A+2*B
            while (y1<=y):
                plot(screen,color,x,y)
                if (d>0):
                    x+=1
                    d+=2*A
                y-=1
                d-=2*B
