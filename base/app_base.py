"""
@author:xue
@time:2020/8/6
@desc:
"""
from base.base import Base


class AppBase(Base):

    def activity(self, page_name, active_name):
        """
        启动Activity
        :param page_name:package包名
        :param active_name:
        """
        self._log.info("启动Activity:".format(page_name, active_name))
        self._driver.start_activity(page_name, active_name)

    def current_activity(self):
        """获取当前Activity"""
        return self._driver.current_activity

    def press_key(self, code):
        """
        按键盘按键，仅支持Android
        :param code: 键盘上每个按键的ascii
        :return:
        """
        self._driver.press_keycode(code)

    def swipe(self, start_x, start_y, end_x, end_y, dur=800):
        """
        滑动操作
        :param start_x: 起始横坐标
        :param start_y: 起始纵坐标
        :param end_x: 终点横坐标
        :param end_y: 终点纵坐标
        :param dur: 在多长时间内完成滑动操作(单位:ms)
        """
        return self._driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=dur)

    def swipe_up(self, dur=500, times=1):
        """
        上划
        :param dur: 滑动时间
        :param times:次数
        """
        s = self._driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.75  # 起点y坐标
        y2 = s['height'] * 0.25  # 终点y坐标
        print('手机的尺寸是： '.format(s))
        for i in range(times):
            self._driver.swipe(x1, y1, x1, y2, dur)

    def swipe_down(self, dur=500, times=1):
        """
        上划
        :param dur: 滑动时间
        :param times:次数
        """
        s = self._driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.25  # 起点y坐标
        y2 = s['height'] * 0.75  # 终点y坐标
        print('手机的尺寸是： '.format(s))
        for i in range(times):
            self._driver.swipe(x1, y1, x1, y2, dur)

    def swipe_left(self, dur=500, times=1):
        """
        上划
        :param dur: 滑动时间
        :param times:次数
        """
        s = self._driver.get_window_size()
        x1 = s['width'] * 0.75
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.25
        print('手机的尺寸是： '.format(s))
        for i in range(times):
            self._driver.swipe(x1, y1, x2, y1, dur)

    def swipe_right(self, dur=500, times=1):
        """
        上划
        :param dur: 滑动时间
        :param times:次数
        """
        s = self._driver.get_window_size()
        x1 = s['width'] * 0.25
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.75
        print('手机的尺寸是： '.format(s))
        for i in range(times):
            self._driver.swipe(x1, y1, x2, y1, dur)
