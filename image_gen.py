# coding: utf-8
import random
from math import sin, cos

from PIL import Image, ImageDraw, ImageFilter

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
    r, g, b = grc(), grc(), grc()
    c1 = (r + 50, g + 50, b + 0, 255)
    c2 = (r + 0, g + 50, b + 50, 255)
    c3 = (r + 50, g + 0, b + 50, 255)

    print(c1, c2, c3)

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


def gen_img(typeof=None, nested=None):
    # type = 1 for squares - by default
    # type = 2  is for circles
    if typeof is not None:
        type = typeof
    else:
        type = random.randint(1, 2)

    colors = gen_rnd_colors()
    if type == 3:
        new_image = Image.new("RGBA", img_size, "rgba(102, 102, 102, 51)")
    else:
        new_image = Image.new("RGBA", img_size, colors[2])

    figure_draw = ImageDraw.Draw(new_image)
    if nested is not None:
        sc_n = nested
    else:
        sc_n = random.randint(2, 7)

    for point in gen_rnd_points():

        x0 = point[0]
        y0 = point[1]

        square_size = random.randint(rnd_min_size, rnd_max_size)

        for sc in range(sc_n, 1, -1):

            dx = int(square_size / 2 / (sc_n - 1) * sc)
            dy = int(square_size / 2 / (sc_n - 1) * sc)

            if sc == sc_n:
                outline_color = colors[1]
            else:
                outline_color = None

            if sc % 2 == 1:
                fill_color = colors[0]
            else:
                fill_color = colors[2]

            if type == 1:
                figure_draw.rectangle((x0 - dx, y0 - dy) + (x0 + dx, y0 + dy), fill=fill_color, outline=outline_color)
            elif type == 2:
                figure_draw.ellipse((x0 - dx, y0 - dy) + (x0 + dx, y0 + dy), fill=fill_color, outline=outline_color)
            elif type == 3:
                transparency = 255
                colors = [(255, 0, 255, transparency), (0, 255, 255, transparency), (204, 51, 255, transparency),
                          (204, 255, 0, transparency), (153, 51, 153, transparency), (255, 255, 51, transparency),
                          (0, 102, 255, transparency), (102, 102, 0, transparency), (0, 153, 102, transparency)]
                outline_color = None
                fill_color = random.choice(colors)
                figure_draw.ellipse((x0 - dx, y0 - dy) + (x0 + dx, y0 + dy), fill=fill_color, outline=outline_color)

    #new_image = new_image.filter(ImageFilter.MinFilter)

    del figure_draw

    return new_image


def gen_bubbles():
    new_image = Image.new("RGBA", img_size, "rgba(102, 102, 102, 153)")

    # fill_color = "rgba(204, 255, 255, 204)"
    # outline_color = "rgba(102, 153, 153, 225)"

    bubbles_draw = ImageDraw.Draw(new_image)

    # bubbles_draw.ellipse((100,100) + (200,200), fill=fill_color, outline=None)

    colors = [(0, 0, 0, 0), (0, 204, 204, 51), (153, 0, 204, 51), (204, 255, 0, 51), (153, 0, 153, 51),
              (0, 102, 255, 51), (102, 1204, 0, 51), (), (), ()]

    x0 = 150
    y0 = 150

    for n in range(6, 1, -1):
        dx = int(100 / 2 / (8 - 1) * n)
        dy = int(100 / 2 / (8 - 1) * n)

        outline_color = None

        fill_color = colors[n - 1]

        bubbles_draw.ellipse((x0 - dx, y0 - dy) + (x0 + dx, y0 + dy), fill=fill_color, outline=outline_color)

    del bubbles_draw

    return new_image


def gen_tree():
    sky_color = "rgba(51, 153, 255, 255)"

    ground_color = "rgba(51, 153, 255, 255)"

    lv1 = "rgba(51, 102, 51, 255)"
    lv2 = "rgba(0, 51, 0, 255)"
    lv3 = "rgba(204, 255, 0, 255)"
    lv4 = "rgba(204, 51, 0, 255)"
    leaves = [lv1, lv2, lv3, lv4]

    grass_color = "rgba(51, 51, 0, 255)"

    fill_color = "rgba(102, 51, 0,255)"
    outline_color = "black"

    new_image = Image.new("RGBA", img_size, sky_color)
    tree_draw = ImageDraw.Draw(new_image)

    w = new_image.width
    h = new_image.height

    tree_points = list()

    # левый нижний скос
    tree_points.append(((random.randint(w / 2 - 60, w / 2 - 48)), h - random.randint(7, 17)))  # tp1
    tree_points.append(((random.randint(w / 2 - 45, w / 2 - 38)), h - random.randint(40, 60)))  # tp2

    # левая нижняя ветка
    tree_points.append(((random.randint(w / 2 - 33, w / 2 - 28)), h / 2 + random.randint(40, 53)))  # tp3
    tp4x, tp4y = (random.randint(w / 2 - 200, w / 2 - 150)), h / 3 + random.randint(0, 70)
    tree_points.append((tp4x, tp4y))  # tp4
    tree_points.append((tp4x + random.randint(3, 7), tp4y - random.randint(3, 7)))  # tp5
    tree_points.append(((random.randint(w / 2 - 27, w / 2 - 25)), h / 2 + random.randint(12, 19)))  # tp6

    # левая верхняя ветка
    tree_points.append(((random.randint(w / 2 - 22, w / 2 - 19)), h / 2 - random.randint(25, 35)))  # tp7
    tp8x, tp8y = (random.randint(w / 2 - 110, w / 2 - 70)), h / 3 - random.randint(23, 50)
    tree_points.append((tp8x, tp8y))  # tp8
    tree_points.append((tp8x + random.randint(3, 7), tp8y - random.randint(3, 7)))  # tp9
    tree_points.append(((random.randint(w / 2 - 18, w / 2 - 15)), h / 2 - random.randint(53, 65)))  # tp10

    # верхняя точка ствола
    tree_points.append(((random.randint(w / 2 - 14, w / 2 - 9)), h / 4 - random.randint(30, 50)))  # tp7
    tree_points.append(((random.randint(w / 2 + 10, w / 2 + 17)), h / 4 - random.randint(30, 50)))  # tp8

    # праваяя верхняя ветка

    # правая нижняя ветка
    tree_points.append(((random.randint(w / 2 + 20, w / 2 + 25)), h / 2 - random.randint(20, 30)))  # tp9
    tp10x, tp10y = (random.randint(w / 2 + 150, w / 2 + 200)), h / 3 + random.randint(-40, 50)
    tree_points.append((tp10x, tp10y))  # tp10
    tree_points.append((tp10x + random.randint(3, 7), tp10y + random.randint(3, 7)))  # tp11
    tree_points.append(((random.randint(w / 2 + 28, w / 2 + 35)), h / 2 + random.randint(0, 10)))  # tp12

    # правый нижний скос
    tree_points.append(((random.randint(w / 2 + 38, w / 2 + 45)), h - random.randint(40, 60)))  # tp13
    tree_points.append(((random.randint(w / 2 + 48, w / 2 + 60)), h - random.randint(7, 17)))  # tp4

    # print(tree_points)

    tree_draw.polygon(tree_points, fill=fill_color, outline=outline_color)
    del tree_draw

    draw_leaves = False
    if draw_leaves:
        leaves_draw = ImageDraw.Draw(new_image)
        fill_color = leaves[2]
        outline_color = leaves[1]

        leaves_points = []

        leaves_points.append((tree_points[3][0] - 15, tree_points[3][1] + 4))
        leaves_points.append((tree_points[3][0] - 15, tree_points[3][1] - 16))
        leaves_points.append((tree_points[3][0] - 4, tree_points[3][1] - 36))
        leaves_points.append((tree_points[3][0] + 12, tree_points[3][1] - 36))
        leaves_points.append((tree_points[3][0] + 37, tree_points[3][1] + 6))

        leaves_draw.polygon(leaves_points, fill=fill_color, outline=outline_color)

        del leaves_draw

    # сетка
    grid = False
    if grid:
        grid_draw = ImageDraw.Draw(new_image)

        grid_draw.line([(w / 2, 0), (w / 2, h)], fill="black")
        grid_draw.line([(0, h / 2), (w, h / 2)], fill="black")

        grid_draw.line([(w / 2 - 100, 0), (w / 2 - 100, h)], fill="black")
        grid_draw.line([(w / 2 + 100, 0), (w / 2 + 100, h)], fill="black")

        grid_draw.line([(0, h / 3), (w, h / 3)], fill="black")
        grid_draw.line([(0, 2 * h / 3), (w, 2 * h / 3)], fill="black")

        del grid_draw

    return new_image


def check_file(fn):
    try:
        open(fn, "r")
        return True
    except (IOError, OSError) as e:
        print("Error: " + str(e))
        return False


def get_counter():
    if check_file("counter"):
        f = open('counter')
        cnt = f.read()
        f.close()
        return cnt


def set_counter(value):
    f = open('counter', 'w')
    f.write(value)
    f.close()


def save_image(image, file=None):
    if file is None:
        cnt = get_counter()
        image_file_name = 'new_image_' + str(cnt) + '.png'
        set_counter(str(int(cnt) + 1))
    else:
        image_file_name = file

    image.save(image_file_name, "PNG")


if __name__ == '__main__':
    save_image(gen_img(), "rnd_test.png")
    # save_image(gen_tree(),"tree_test.png")
    # save_image(gen_bubbles(), "bubbles_test.png")
