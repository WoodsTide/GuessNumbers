#  Copyright (c) 2023.森汐, lnc. All Rights Reserved.
#  @作者        ：森汐(WoodsTide)
#  @邮件        ：Tewn.three.seven@gmail.com
#  @文件        ：项目[GuessNumbers]-main.py
#  @修改时间        ：2023-05-01 18:37:16
#  @上次修改        ：2023/5/1 下午6:37

import random


def is_right(guess, answer):
    """
    判断用户猜测的数字是否正确

    :param guess: 用户输入的数字
    :param answer: 正确的答案
    :return: 如果用户猜对了则返回 True，否则返回 False
    """
    if guess < answer:
        print("你猜的数太小了！")
        return False
    elif guess > answer:
        print("你猜的数太大了！")
        return False
    else:
        print("你猜对了！")
        return True


def is_int(num_str):
    """
    判断一个字符串是否为整数

    :param num_str: 待判断的字符串
    :return: 如果该字符串是整数，则返回 True，否则返回 False
    """
    return num_str.lstrip('-').isdigit()


def play_game(function_min_num, function_max_num):
    """
    猜数字游戏

    :param function_min_num: 随机数最小值
    :param function_max_num: 随机数最大值
    """
    times = 0  # 猜测次数
    game_over = False

    while not game_over:
        answer = random.randint(function_min_num, function_max_num)
        guess_right = False
        print("一个新的随机数已经生成！")

        while not guess_right:
            guess = input(f"\n请输入一个{function_min_num}到{function_max_num}之间的数（输入 'q' 结束游戏）：")

            if guess == 'q':
                print(f"本次游戏答案：{answer}")
                game_over = True
                break

            if not is_int(guess):
                print("请输入一个整数！")
                continue

            guess = int(guess)
            if guess < function_min_num or guess > function_max_num:
                print("输入不合法，请输入合法数字范围！")
                continue

            times += 1
            guess_right = is_right(guess, answer)

        if not game_over:
            print(f"你共猜了{times}次！\n")


def settings():
    """
    猜数字游戏设置菜单
    """
    while True:
        print("\n==========================")
        print("\t猜数字游戏设置菜单\n")
        print("选项\t\t\t\t值")
        print(f"min:最小随机数\t\t{min_num}")
        print(f"max:最大随机数\t\t{max_num}")
        print("q:退出设置菜单")
        print("==========================")

        option = input("\n请输入要修改的选项：")

        if option == 'q':
            print("已退出设置菜单！\n")
            break

        if option == 'min':
            new_min = input("请输入新的最小随机数：")
            if is_int(new_min):
                new_min = int(new_min)
                if new_min <= max_num:
                    globals()["min_num"] = new_min  # 使用 min_num 全局变量来更新 min_num 的值
                    print(f"最小随机数已修改为：{min_num}\n")
                else:
                    print("新的最小随机数不能超出原最大随机数，请重新输入！")
            else:
                print("输入不合法，请输入一个整数！")

        elif option == 'max':
            new_max = input("请输入新的最大随机数：")
            if is_int(new_max):
                new_max = int(new_max)
                if new_max >= min_num:
                    globals()["max_num"] = new_max  # 使用 max_num 全局变量来更新 max_num 的值
                    print(f"最大随机数已修改为：{max_num}\n")
                else:
                    print("新的最大随机数不能低于原最小随机数，请重新输入！")
            else:
                print("输入不合法，请输入一个整数！")

        else:
            print("输入不合法，请输入有效选项！")


if __name__ == '__main__':
    min_num = 1
    max_num = 100

    while True:
        print("\n===========================")
        print("\t欢迎来到猜数字游戏！\n")
        print("选项\t\t\t\t操作")
        print("p:\t\t开始新游戏")
        print("s:\t\t打开游戏设置菜单")
        print("q:\t\t退出游戏")
        print("===========================")

        choice = input("\n请输入你的选项：")

        if choice == 'q':
            print("再见！")
            break

        if choice == 'p':
            play_game(min_num, max_num)

        elif choice == 's':
            settings()

        else:
            print("请输入有效选项！")
