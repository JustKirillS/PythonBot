import time

import cv2
import numpy as np
from PIL import ImageGrab as grab


def find_health_bar():
    bg = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('health.jpg', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(bg, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    return loc


def print_fps(last_time):
    fps = 1 / (time.time() - last_time)
    print('FPS: {}'.format(fps))


last_time = time.time()
while True:
    width = 700
    height = 500
    point = [1920 - width, 1080 - height]
    screen = np.array(grab.grab(bbox=(point[0], point[1], point[0] + width, point[1] + height)))

    loc = find_health_bar()
    print(loc)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(screen, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

    # print_fps(last_time)
    last_time = time.time()

    cv2.imshow('preview', screen)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
