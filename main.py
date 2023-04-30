#  Copyright (c) 2023.森汐, lnc. All Rights Reserved.
#  @作者        ：森汐(WoodsTide)
#  @邮件        ：Tewn.three.seven@gmail.com
#  @文件        ：项目[GuessNumbers]-main.py
#  @修改时间        ：2023-04-30 15:36:25
#  @上次修改        ：2023/4/30 下午3:36

import random


# 定义判断输入数字是否正确的函数
def determine(importation, randomized):
    if importation < randomized:
        print("你猜的数太小了！\n")
        return False
    elif importation > randomized:
        print("你猜的数太大了！\n")
        return False
    else:
        print("你猜对了！\n")
        return True


i = True
j = False
times = 0

while i:
    j = False
    randomNumber = random.randint(1, 100)
    while not j:
        try:
            inputtedNumber = int(input("请输入一个1到100之间的数>>>"))
        except ValueError:
            print("请输入一个整数！\n")
            continue

        if inputtedNumber < 1 | inputtedNumber > 100:
            print("输入值超出范围！\n")
            continue

        j = determine(inputtedNumber, randomNumber)
        times += 1
        if j:
            print(f"你一共猜了{times}次。")
            i = False

    print("Game Over!")
