# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:46:31 2024

@author: p1241
"""

class Role :
    
    def __init__(self,name,HP,MP):
        
        self.__name = name #.__ 這個是程式私有化的概念，不給人家去改程式
        
        self.__HP = HP
        
        self.__MP = MP
        
    def getName(self):
        
        return self.__name
    
    def getHP(self):
        
        return self.__HP

    def getMP(self):
        
        return self.__MP
    
    
class Dwarves(Role):  #矮人
    
    def fight(self):
        
        print("斧頭攻擊")
        
    def skill(self):
        
        print("矮人斬擊")
        
    def skill_2(self):
        
        print("矮人衝刺")
        
    def skill_3(self):
        
        print("致命爆破")    
        
class Elves(Role):  #精靈
    
    def fight(self):
        
        print("弓箭攻擊")
        
    def skill(self):
        
        print("連續射擊")
        
    def skill_2(self):
        
        print("三連箭")
        
    def skill_3(self):
        
        print("致命射擊")   
        

        
class Human(Role):  #人類
    
    def fight(self):
        
        print("大劍攻擊")
        
    def skill(self):
        
        print("月光斬")
        
    def skill_2(self):
        
        print("太陽斬")
        
    def skill_3(self):
        
        print("星爆氣流斬")   
        
        
class Hobbits(Role):  #哈比人
    
    def fight(self):
        
        print("匕首攻擊")
        
    def skill(self):
        
        print("飛天匕首")
        
    def skill_2(self):
        
        print("錢鏢")
        
    def skill_3(self):
        
        print("咕嚕型態")   
        
