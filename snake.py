import pygame
import random
import time
pygame.init()
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
lol=(45,78,52)

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('slither')




clock=pygame.time.Clock()
block_size=10
fps=30
font=pygame.font.SysFont(None,25)
def snake(block_size,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])
        

    



def message(msg,color):
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])
       

def gameloop():
    snakelist=[]
    

    snakelength=1
    gameover=False
    gameExit= False
    lead_x=display_width/2
    lead_x_change=0
    lead_y_change=0
    lead_y=display_height/2
    randapplex=round(random.randint(0,display_width-block_size)/10)*10
    
    randappley=round(random.randint(0,display_height-block_size)/10)*10
    while not gameExit:
        while gameover== True:
            gameDisplay.fill(white)
            message("press Y or N for continue",red)
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
                elif event.key==pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                elif event.key==pygame.K_DOWN:
                    lead_y_change=+block_size
                    lead_x_change=0
                elif event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
        if lead_x>=display_width or lead_x<= 0 or lead_y>=display_height or lead_y<=0:
            gameover=True
                
                
            
                
                

        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gameDisplay.fill(white)
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

        if(lead_x==randapplex and lead_y==randappley):
            randapplex=round(random.randint(0,display_width-block_size)/10)*10
    
            randappley=round(random.randint(0,display_height-block_size)/10)*10
            snakelength+=1
            
      
        clock.tick(fps)
            
            
               
               
            





    message("you suck",red)
    
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
gameloop()
