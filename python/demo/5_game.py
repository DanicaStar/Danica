import random
import time
Li_score=0    # “Li_score” 代表李逍遥赢的局数
BOSS_score=0    # “BOSS_score” 代表拜月教主赢的局数
for i in range(1,4):
    time.sleep(1)
    print("现在进行第"+str(i)+"局")

    #生成随机属性
    Li_blood = random.randint(100,150) # “freeLi_life” 代表李逍遥血量
    Li_power = random.randint(20,30) # “freeLi_attack” 代表李逍遥攻击
    BOSS_blood = random.randint(100,150) # “BOSS_life” 代表拜月教主血量
    BOSS_power = random.randint(20,30) # “BOSS_attack” 代表拜月教主攻击

    #展示双方属性
    print("【李逍遥】\n血量：%s\n攻击%s" %(Li_blood,Li_power))
    print('------------------------')
    time.sleep(1)
    print("【拜月教主】\n血量：%s\n攻击%s" %(BOSS_blood,BOSS_power))
    print('------------------------')
    time.sleep(1)
    
    #PK计算
    while Li_blood>0 and BOSS_blood>0:
        Li_blood=Li_blood -BOSS_power
        BOSS_blood=BOSS_blood-Li_power
        print("【李逍遥】\n血量：%s\n攻击%s" %(Li_blood,Li_power))
        print("【拜月教主】\n血量：%s\n攻击%s" %(BOSS_blood,BOSS_power))
        print('------------------------')
        time.sleep(2)

    #打印战果
    if Li_blood>0 and BOSS_blood<=0:
        Li_score=Li_score+1
        print("拜月教主挂了，李逍遥赢了")
    elif Li_blood<=0 and BOSS_blood>0:
        BOSS_score=BOSS_score+1
        print("悲催，拜月教主把李逍遥干掉了！")
    else:
        print("哎呀，李逍遥和拜月教主同归于尽了！")
if Li_score>BOSS_score:
    time.sleep(1)
    print("【 大战3个回合：李逍遥赢了！】")
elif Li_score<BOSS_score:
    time.sleep(1)
    print("【 大战3个回合：李逍遥输了！】")
else:
    time.sleep(1)
    print("【大战3个回合：平局！】")
