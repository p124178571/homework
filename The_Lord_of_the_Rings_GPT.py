# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 19:47:25 2024

@author: USER
"""

from Role_GPT import Dwarves, Elves, Human
import random

if __name__ == "__main__":
    player = []
    com = []

    for i in range(3):
        p = int(input("矮人選:1,精靈選:2,人類選:3"))
        name = input("輸入角色姓名:")

        if p == 1:
            player.append(Dwarves(name, 100, 20))
        elif p == 2:
            player.append(Elves(name, 100, 50))
        else:
            player.append(Human(name, 100, 30))

    # 電腦
    com_names = ["武小道", "Micky", "龍堅", "一虎", "柴大壽", "柴八戒", "阿啪"]
    for i in range(3):
        c = random.randint(1, 3)
        com.append(Dwarves(com_names[i], 100, 20) if c == 1 else
                   Elves(com_names[i], 100, 50) if c == 2 else
                   Human(com_names[i], 100, 30))

    while len(player) > 0 and len(com) > 0:
        for character in player + com:
            print(f"{character.getName()}的血量: {character.getHP()}")
        
        attacker = random.choice(player + com)
        target = random.choice(player + com)

        if attacker in player:
            print(f"玩家 {attacker.getName()} 使出:", end="")
        else:
            print(f"電腦 {attacker.getName()} 使出:", end="")

        if random.randint(1, 10) == 3:
            attacker.skill()
            damage = random.randint(10, 15)
        elif random.randint(1, 30) == 15:
            attacker.skill_3()
            damage = random.randint(99, 100)
        else:
            attacker.fight()
            damage = random.randint(5, 10)

        target.setHP(target.getHP() - damage)
        print(f"{target.getName()} 的血量剩: {target.getHP()}")

        # 移除血量為0的角色
        if target.getHP() <= 0:
            if target in player:
                print(f"{target.getName()} 被擊敗，電腦獲勝！")
            else:
                print(f"{target.getName()} 被擊敗，玩家獲勝！")
            if target in player:
                player.remove(target)
            else:
                com.remove(target)

# 判斷遊戲結果
if len(player) > 0:
    print("玩家獲勝！")
else:
    print("電腦獲勝！")