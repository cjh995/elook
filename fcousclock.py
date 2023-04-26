import time
import os

def concentration_clock(minutes):
    seconds = minutes * 60
    while seconds > 0:
        os.system('cls' if os.name == 'nt' else 'clear')  # 清屏操作，兼容Windows和Linux/MacOS
        print("专注倒计时: {} 分钟".format(seconds // 60))
        time.sleep(1)
        seconds -= 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print("专注时间结束！")

# 设置专注时长，单位为分钟
concentration_time = 25
concentration_clock(concentration_time)
