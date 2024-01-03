# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 23:43:39 2024

@author: p1241
"""

from Role import Dwarves,Elves,Human

import random

if __name__ == "__main__":
    
    player = list()
    
    com = list()
    
    for i in range(3):
        
        p = int(input("矮人選:1,精靈選:2,人類選:3"))
        
        name = input("輸入角色姓名:")
        
        if p == 1:
            
            player.append(Dwarves(name,100,20))
            
        elif p == 2:
            
            player.append(Elves(name,100,50))            

            
        else:
            
            player.append(Human(name,100,30))

    #電腦
    
    for i in range(3):
        
        c = random.randint(1,3)
        
        name = ["武小道","Micky","龍堅","一虎","柴大壽","柴八戒","阿啪"]
        
        random.choice(name) #從串列中隨機抓取裡面的其中一個項目值
        
        if c == 1:
            
            com.append(Dwarves(name,100,20))
            
        elif c == 2:
            
            com.append(Elves(name,100,50))       
            
        else:
            
            com.append(Human(name,100,30))
            
            
    while len(player) > 0 and len(com) > 0:

        n = random.randint(1,100) #1~100隨機亂數

        if n % 2 == 0 :       #攻擊順序是隨機的，迴圈誰的亂數能整除2  誰就攻擊
        
            print(player[0].getName(),"使出:",end="")

            if random.randint(1,10) == 3:
                
                player[0].skill()
                
                boold = random.randint(10,15)
                
                
            elif random.randint(1,30) == 15:
                
                player[0].skill_3()
                
                boold = random.randint(99,100)                

                 
            else:
                
                 player[0].fight()
            
                 boold = random.randint(5,10)  #設定攻擊血量，用亂數5~10滴血
                   
         
            player[0].setHP(player[0].getHP()-boold)  #Ad打Sm  ，所以Sm會扣血
            
            print(player[0].getName(),"的血量剩:",player.getHP())  #Sm扣血後會印出
        
        else:
            
            print(com[0].getName(),"使出:",end="")
            
            if random.randint(1,10) == 3:
                
                com.skill()
                
                boold = random.randint(10,15)
                
                
            elif random.randint(1,30) == 15:
                
                com.skill_3()
                
                boold = random.randint(99,100)                

                 
            else:
                
                 com.fight()
            
                 boold = random.randint(5,10)  #設定攻擊血量，用亂數5~10滴血
                   
         
            com.setHP(com.getHP()-boold)  #Ad打Sm  ，所以Sm會扣血
            
            print(com.getName(),"的血量剩:",com.getHP()) 
                 











if len(player) < 0:
    
    print("玩家","Win")
    
else:
    print("電腦","Win")

