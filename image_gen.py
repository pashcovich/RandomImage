# coding: utf-8
import random
from math import sin, cos

from PIL import Image, ImageDraw

img_width = 640
img_height = 480
img_size = (img_width, img_height)

rnd_min_size = 50
rnd_max_size = 80

COLOR1 = (44, 117, 255, 255)
COLOR2 = (97, 152, 255, 255)
COLOR3 = (0, 87, 255, 255)


def sinx(value):
    return sin(value / 2)


def cosx(value):
    return cos(value / 2)


def sin3x(value):
    return sin(3 * value / 4)


def cos3x(value):
    return cos(3 * value / 4)


def gen_rnd_colors():
    grc = lambda: random.randint(0, 255)
    t1, t2, t3 = grc(), grc(), grc()
    c1 = (t1 + 50, t2 + 50, t3 + 0, 255)
    c2 = (t1 + 0, t2 + 50, t3 + 50, 255)
    c3 = (t1 + 50, t2 + 0, t3 + 50, 255)

    return [c1, c2, c3]


def gen_rnd_points():
    xy = []

    for x in range(0, img_width, int(0.6 * rnd_min_size)):

        for step in range(0, img_height, int(0.6 * rnd_min_size)):
            rnd_x_shift = random.randrange(-6, 6, 5)
            rnd_y_shift = random.randrange(-6, 6, 5)

            y = 0
            x += rnd_x_shift
            for cnt in range(0, 4):
                rnd = random.randint(0, 4)

                if rnd == 0:
                    y += 2 * sinx(x)
                elif rnd == 1:
                    y += 2 * cosx(x)
                elif rnd == 2:
                    y += 2 * sin3x(x)
                elif rnd == 3:
                    y += 2 * cos3x(x)

            y += step
            y += rnd_y_shift
            xy.append((x, y))
    list_xy = list(set(xy))
    random.shuffle(list_xy)
    random.SystemRandom().shuffle(list_xy)
    return list_xy


def gen_img(type=1):
    # type = 1 for squares - by default
    # type = 2  is for circles

    colors = gen_rnd_colors()

    new_image = Image.new("RGBA", img_size, colors[0])

    figure_draw = ImageDraw.Draw(new_image)

    for point in gen_rnd_points():

        x0 = point[0]
        y0 = point[1]

        square_size = random.randint(rnd_min_size, rnd_max_size)

        sc_n = 6

        for sc in range(sc_n, 1, -1):

            dx = int(square_size / 2 / (sc_n - 1) * sc)
            dy = int(square_size / 2 / (sc_n - 1) * sc)

            if sc == sc_n:
                outline_color = colors[1]
            else:
                outline_color = None

            if sc % 2 == 1:
                blue_color = colors[0]
            else:
                blue_color = colors[2]

            if type == 1:
                figure_draw.rectangle((x0 - dx, y0 - dy) + (x0 + dx, y0 + dy), fill=blue_color, outline=outline_color)
            elif type == 2:
                figure_draw.ellipse((x0 - dx, y0 - dy) + (x0 + dx, y0 + dy), fill=blue_color, outline=outline_color)

    del figure_draw

    return new_image


def get_increment():
    f = open('increment')
    inc = f.read()
    f.close()
    # print("Last increment = " + inc)
    return inc


def set_increment(value):
    f = open('increment', 'w')
    f.write(value)
    f.close()


def save_image(image, file=None):
    if file is None:
        inc = get_increment()
        image_file_name = 'new_image' + str(inc) + '.png'
        set_increment(str(int(inc) + 1))
    else:
        image_file_name = file

    image.save(image_file_name, "PNG")


if __name__ == '__main__':
    save_image(gen_img(2))
