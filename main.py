#  Copyright (c) 2023.森汐, lnc. All Rights Reserved.
#  @作者        ：森汐(WoodsTide)
#  @邮件        ：Tewn.three.seven@gmail.com
#  @文件        ：项目[GuessNumbers]-main.py
#  @修改时间        ：2023-05-01 17:00:53
#  @上次修改        ：2023/5/1 下午4:46

import random


# 定义判断输入数字是否正确的函数
def is_right(importation, randomized):
    if importation < randomized:
        print("你猜的数太小了！\n")
        return False
    elif importation > randomized:
        print("你猜的数太大了！\n")
        return False
    else:
        print("你猜对了！\n")
        return True


# 定义判断输入是否为整数的函数
def is_int(enter):
    if enter.lstrip('-').isdigit():  # lstrip()方法去除左边的字符，只留下数字；isdigit()方法返回布尔值，判断是否是数字
        return True
    else:
        return False


minRandom = 1  # 随机数范围的最小值
maxRandom = 100  # 随机数范围的最大值

setting = True
changing = True
run = True  # 游戏是否运行的标志
times = 0  # 猜测次数

while run:
    start = input("键入P(Play)或S(Setting)来开始游戏或进行设置>>>")

    if start.lower() == "p":  # 支持大小写的输入
        game = True
        right = False

        while game:
            randomNumber = random.randint(minRandom, maxRandom)  # 随机生成一个数字
            # print(randomNumber) # 调试时可以打印出生成的数字
            while not right:
                inputted = input(f"请输入一个{minRandom}到{maxRandom}之间的数(键入exit来退出)>>>")

                if inputted.lower() == "exit":
                    print(f"本次生成的随机数是{randomNumber}")
                    break
                else:
                    if is_int(inputted):
                        inputted = int(inputted)
                    else:
                        print("请输入一个整数!\n")
                        continue

                    if inputted < minRandom or inputted > maxRandom:
                        print("输入值超出范围！\n")
                        continue

                    times += 1
                    if is_right(inputted, randomNumber):
                        print(f"你一共猜了{times}次。")
                        right = True
                        del start  # 清除该变量，再次开始游戏时初始化参数
            print("Game Over!\n")
            game = False

    elif start.lower() == "s":
        while setting:
            print("================")
            print("\t设置菜单\n")
            print("项目\t\t\t\t值")
            print(f"min:最小随机数\t{minRandom}")
            print(f"max:最大随机数\t{maxRandom}")
            print("================")

            option = input("\n请键入要修改的项目(键入exit来退出)>>>")

            if option.lower() == "exit":
                print("已退出设置菜单！\n")
                break

            while changing:

                if option.lower() == "min":
                    entering = input("请输入值>>>")

                    if is_int(entering):
                        entering = int(entering)

                        if entering > maxRandom:
                            print("最小值大于最大值，请重新输入！\n")
                            continue
                        elif entering == maxRandom:
                            print("最小值等于最大值，请重新输入！\n")
                        else:
                            minRandom = entering
                            print(f"最小值已成功修改为{entering}\n")
                        break
                    else:
                        print("请输入一个整数!\n")

                elif option.lower() == "max":
                    entering = input("请输入值>>>")

                    if is_int(entering):
                        entering = int(entering)

                        if entering < minRandom:
                            print("最大值小于最小值，请重新输入！\n")
                        elif entering == minRandom:
                            print("最大值等于最小值，请重新输入！\n")
                        else:
                            maxRandom = entering
                            print(f"最大值已成功修改为{entering}\n")
                        break
                else:
                    print("请输入一个正确的项目！\n")
                    del option  # 清除该变量，重新进入选项菜单
                    break
        continue
