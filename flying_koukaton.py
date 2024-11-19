import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像surfaceを作成する
    bg2_img = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png") #こうかとん画像surfaceを作成する
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    screen.blit(kk_img,kk_rct)

    tmr = 0
    
    while True:
        x = -1
        y = 0
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        #print(key_lst[pg.K_UP],key_lst[pg.K_DOWN],key_lst[pg.K_LEFT],key_lst[pg.K_RIGHT])
        if key_lst[pg.K_RIGHT]:
            x = 1
        elif key_lst[pg.K_LEFT]:
            x = -1
        elif key_lst[pg.K_DOWN]:

            y = 1
        elif key_lst[pg.K_UP]:
            y = -1
        else:
            x = -1
        kk_rct.move_ip((x,y))
            

       
        

        screen.blit(bg_img, [ -(tmr%3200), 0])
        screen.blit(bg2_img,[ -(tmr%3200)+1600,0])
        screen.blit(bg_img, [ -(tmr%3200)+3200,0])
        screen.blit(bg2_img,[ -(tmr%3200)+4800,0])


        screen.blit(kk_img,kk_rct)
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)
  


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()