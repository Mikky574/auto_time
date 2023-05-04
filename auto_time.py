import random
import datetime
import time
import os


def fun1():
    # 在这里实现需要执行的函数逻辑
    print("Hello, world!")


def run():
    # 记录上次运行的时间
    if os.path.exists("last_run.txt"):
        with open("last_run.txt", "r") as f:
            last_run_str = f.read()
            if last_run_str:
                last_run = datetime.datetime.strptime(
                    last_run_str, "%Y-%m-%d %H:%M:%S")
                # 改为这周的星期一，方便后续处理
                last_run -= datetime.timedelta(days=last_run.weekday())
            else:
                # 第一次运行
                last_run = datetime.datetime.min
    else:
        # 第一次运行
        with open("last_run.txt", "w") as f:
            last_run = datetime.datetime.min
            f.write("")

    # 计算本周周一和周二的日期
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())  # 周一的日期
    tuesday = monday + datetime.timedelta(days=1)  # 周二的日期
    if last_run.date() >= monday:
        print("This week has already run.")
        return

    if today > tuesday:  # 过时间了，本周不执行
        print("Today is %s. It's after Tuesday" %
              (datetime.date.today().weekday()))
        return

    # 随机选择一个在周一到周二之间的时间（但不能是凌晨0点到6点之间）
    while True:
        rand_time = datetime.datetime.combine(random.choice([monday, tuesday]), datetime.time(
            hour=random.randint(7, 23), minute=random.randint(0, 59)))
        now = datetime.datetime.now()
        if rand_time >= datetime.datetime.now():
            break
        elif datetime.datetime.now().date() > tuesday:
            return  # 以防幺蛾子

    # 等待到随机选择的时间后运行函数
    delta = rand_time - now
    if delta.total_seconds() > 0:
        print("Next run time:", rand_time)
        time.sleep(delta.total_seconds())

    fun1()

    # 更新本次运行的时间
    with open("last_run.txt", "w") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print("Done.")


if __name__ == '__main__':
    while True:
        run()
        # 等待一天后再次运行
        time.sleep(24 * 3600)
