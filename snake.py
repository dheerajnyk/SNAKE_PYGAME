import pygame
import random
import time
pygame.init()
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
lol=(45,78,52)
img=pygame.image.load('snakehead.png')
display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('slither')




clock=pygame.time.Clock()
block_size=20
fps=15
direction="right"
smallfont=pygame.font.SysFont(None,25)
mediumfont=pygame.font.SysFont("comicsansms",55)
largefont=pygame.font.SysFont("comicsansms",80)
def game_intro():
    intro = True
    
    while intro:

        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_y):
                    
                    intro=False
                if(event.key==pygame.K_n):
                    pygame.quit()
                    quit()
                


        
        gameDisplay.fill(white)
        message("WELCOME HUMAN",
                green,
                -100,"large")
        message("just eat apples!!!!",
                black,
                30,
                "small")
        message("and don't run away from the screen",
                black,
                50,
                "small")
        message("ARE YOU READY (Y/N)",
                red,
                90,
                "medium")
        pygame.display.update()
        clock.tick(15)
    
    

def snake(block_size,snakelist):
    if(direction=="right"):
        head=pygame.transform.rotate(img,270)
    if(direction=="left"):
        head=pygame.transform.rotate(img,90)
    if(direction=="up"):
        head=img
    if(direction=="down"):
        head=pygame.transform.rotate(img,180)
    
    
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])
        
def text_objects(text,color,size='small'):
    if(size=="small"):
        textsurface=smallfont.render(text,True,color)
    if(size=="medium"):
        textsurface=mediumfont.render(text,True,color)
    if(size=="large"):
        textsurface=largefont.render(text,True,color)
    return textsurface,textsurface.get_rect()

    



def message(msg,color,y_displace=0,size="small"):
   textsurf,textrect=text_objects(msg,color,size)
   #textrect.center=(0),(0)+y_displace
   textrect.center=(display_width/2),(display_height/2)+y_displace
   gameDisplay.blit(textsurf,textrect)
       

def gameloop():
    snakelist=[]
    global direction

    snakelength=1
    gameover=False
    gameExit= False
    lead_x=display_width/2
    lead_x_change=10
    lead_y_change=0
    lead_y=display_height/2
    randapplex=round(random.randint(0,display_width-block_size)/10)*10
    
    randappley=round(random.randint(0,display_height-block_size)/10)*10
    while not gameExit:
        while gameover== True:
            gameDisplay.fill(white)
            message("GAME OVER",red,+50,"large")
            message("Press Y to play again and N to quit",black,-50,'medium')
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_n:
                        gameExit=True
                        gameover=False

                    elif event.key== pygame.K_y:
                        gameloop()
                    
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
               gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change=-block_size
                    lead_y_change=0
                    direction="left"
                elif event.key==pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                    direction="right"
                elif event.key==pygame.K_DOWN:
                    lead_y_change=+block_size
                    lead_x_change=0
                    direction="down"
                elif event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
                    direction="up"
        if lead_x>=display_width or lead_x<= 0 or lead_y>=display_height or lead_y<=0:
            gameover=True
                
                
            
                
                

        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gameDisplay.fill(white)
        applethickness=30
        pygame.draw.rect(gameDisplay,red,[randapplex,randappley,block_size,block_size])
        
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)




        
        if(len(snakelist)>snakelength):
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment==snakehead:
                gameover=True
            
            

        snake(block_size,snakelist)
        

        pygame.display.update()

        if lead_x > randapplex and lead_x<randapplex+applethickness or lead_x+block_size>randapplex and lead_x+block_size<randapplex+applethickness:
            
            if lead_y > randappley and lead_y<randappley+applethickness or lead_y+block_size>randappley and lead_y+block_size<randappley+applethickness:
                randapplex=round(random.randint(0,display_width-block_size)/10)*10
                randappley=round(random.randint(0,display_height-block_size)/10)*10
                snakelength+=1
            
        
      







        clock.tick(fps)
            
            
               
               
            





    message("NEVER SAY QUIT !!!!",black)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
game_intro()
gameloop()
