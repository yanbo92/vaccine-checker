import atomac
import requests
import time

if __name__ == '__main__':
    automator = atomac.getAppRefByBundleId('com.tencent.xinWeChat')
    window_list = automator.windows()
    window = None
    for w in window_list:
        if "门诊地址列表" in str(w):
            window = w
    refreshButton = window.findFirstR(AXHelp='刷新')
    count = 1
    while True:
        print("第{}次刷新：".format(count))
        refreshButton.Press()
        time.sleep(5)
        bookableText = window.findFirstR(AXValue='可预约')
        if bookableText:
            print("可预约！")
            requests.get("https://sctapi.ftqq.com/XXXXXXXXXXXXXXXXXX.send?title=GotVaccine!")
            # 上面这是个方糖推送，你可以改成自己的key 或者 换成飞书、钉钉之类的推送方式
        else:
            print("已约满。。。。。")
        count = count + 1
        time.sleep(60)

