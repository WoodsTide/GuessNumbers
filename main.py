#  Copyright (c) 2023.森汐, lnc. All Rights Reserved.
#  @作者        ：森汐(WoodsTide)
#  @邮件        ：Tewn.three.seven@gmail.com
#  @文件        ：项目[main.py]-main.py
#  @修改时间        ：2023-05-07 13:12:09
#  @上次修改        ：2023/5/7 下午1:12

import os
import pickle
import random
from time import sleep


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# 读取配置文件，获取随机数范围
def read_config():
    min_num, max_num = 1, 100

    if os.path.isfile("config.cg"):
        config_file = open('config.cg', 'rb')

        try:
            min_num = pickle.load(config_file)
            max_num = pickle.load(config_file)

        except pickle.UnpicklingError:
            clear_console()
            print("无法正确读取配置文件！")
            write_config(min_num, max_num)
            print(f"随机数范围：从 {min_num} 到 {max_num} 。")

        else:
            clear_console()
            print("已从配置文件自动读取数据。")
            print(f"随机数范围：从 {min_num} 到 {max_num} 。")

            config_file.close()

    else:
        clear_console()
        print("无法正确读取配置文件！")
        write_config(min_num, max_num)
        print(f"随机数范围：从 {min_num} 到 {max_num} 。")

    return min_num, max_num


# 写入配置文件
def write_config(min_num, max_num):
    config_file = open('config.cg', 'wb')

    pickle.dump(min_num, config_file)
    pickle.dump(max_num, config_file, -1)

    config_file.close()
    print("已保存配置文件!")


# 判断用户猜测的数字是否正确
def is_right(guess, answer):
    if guess < answer:
        print("你猜的数太小了！")
        return False

    elif guess > answer:
        print("你猜的数太大了！")
        return False

    else:
        print("\n你猜对了！")
        return True


# 判断一个字符串是否为整数
def is_int(num_str):
    return num_str.lstrip('-').isdigit()


# 猜数字游戏主程序
def play_game(min_num, max_num):
    times = 0
    game_over = False

    while not game_over:
        answer = random.randint(min_num, max_num)
        guess_right = False
        print("一个新的随机数已经生成！")

        while not guess_right:
            guess = input(
                f"\n请输入一个{min_num}到{max_num}之间的数（输入 'q' 结束游戏）：")

            if guess == 'q':
                print(f"本次游戏答案：{answer}")
                sleep(2)
                game_over = True
                break

            if not is_int(guess):
                print("请输入一个整数！")
                continue

            guess = int(guess)
            if guess < min_num or guess > max_num:
                print("输入不合法，请输入合法数字范围！")
                continue

            times += 1
            guess_right = is_right(guess, answer)

        if not game_over:
            print(f"你共猜了{times}次！\n")
            sleep(2)
            break


# 猜数字游戏设置菜单
def settings():
    while True:
        print("\n==========================")
        print("猜数字游戏设置菜单\n")
        print("选项\t\t值")
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
                    # 更新全局变量值
                    globals()["min_num"] = new_min
                    print(f"最小随机数已修改为：{min_num}")
                    write_config(min_num, max_num)

                    sleep(1)
                    clear_console()
                else:
                    print("新的最小随机数不能超出原最大随机数，请重新输入！")

                    sleep(1)
                    clear_console()

            else:
                print("输入不合法，请输入一个整数！")
                sleep(1)
                clear_console()

        elif option == 'max':
            new_max = input("请输入新的最大随机数：")

            if is_int(new_max):
                new_max = int(new_max)

                if new_max >= min_num:
                    # 更新全局变量值
                    globals()["max_num"] = new_max
                    print(f"最大随机数已修改为：{max_num}")
                    write_config(min_num, max_num)

                    sleep(1)
                    clear_console()
                else:
                    print("新的最大随机数不能低于原最小随机数，请重新输入！")

                    sleep(1)
                    clear_console()

            else:
                print("输入不合法，请输入一个整数！")

                sleep(1)
                clear_console()

        else:
            print("输入不合法，请输入有效选项！")

            sleep(1)
            clear_console()


def choice():
    while True:
        clear_console()
        print("\n===========================")
        print("欢迎来到猜数字游戏！\n")
        print("选项\t\t操作")
        print("p:\t\t开始新游戏")
        print("s:\t\t打开游戏设置菜单")
        print("q:\t\t退出游戏")
        print("===========================")

        choice = input("\n请输入你的选项：")

        if choice == 'q':
            clear_console()
            print("再见！")
            break

        if choice == 'p':
            clear_console()
            play_game(min_num, max_num)

        elif choice == 's':
            clear_console()
            settings()

        else:
            print("请输入有效选项！")

            sleep(1)
            clear_console()


if __name__ == '__main__':
    min_num, max_num = read_config()

    choice()
