# -*- coding: utf-8 -*-

import cv2

gain = 10
offset_x= 0.2
offset_green = 0.6

def sigmoid(x, gain=1, offset_x=0):
    return ((np.tanh(((x + offset_x) * gain) / 2) + 1) / 2)

def colorBarRGB(x):
    x = (x * 2) - 1
    red = sigmoid(x, gain, -1 * offset_x)
    blue = 1 - sigmoid(x, gain, offset_x)
    green = sigmoid(x, gain, offset_green) + (1 - sigmoid(x, gain, -1 * offset_green))
    green = green - 1.0
    return (255 * blue, 255 * green, 255 * red)

def conv_heatcolor(val):
    return colorBarRGB(float(val) / max_temp)


class info_point:

    def __init__(self, point_name, point_coord, point_type):
        self.name = point_name
        self.coord = point_coord
        self.type = point_type

    def match_name(self, name):
        return self.name == name


class visualizer:

    def __init__(self):
        self.points = []

    # 下絵を読み込む
    def set_canvas(self, filename):
        self.canvas_path = filename
        self.canvas = cv2.imread(filename)

    # 表示する座標を追加する
    # 名前に重複があればNoneを返す
    def add_point(self, point_name, point_coord, point_type=0):
        for point in self.points:
            if point.match_name(point_name):
                return None
        self.points.append(info_point(point_name, point_coord, point_type))
        return self.points

    # 表示する座標を削除する
    def del_point(self, point_name):
        result = False
        for i, point in enumerate(self.points):
            if point.match_name(point_name):
                self.points.pop(i)
                break
        return self.points

