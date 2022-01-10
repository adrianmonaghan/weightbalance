import sys
from PIL import Image, ImageDraw
from aircrafts.r44 import R44


def make_image(info):
    pos1 = (76, 347, 1500, 91)  # x pixel(lon) y pixel (weight), weight value of "origin", lon value of "origin
    pos2 = (226, 317, 1600, 95)  # same as above
    pos3 = (76, 498, 0, 91)  # x pixel (lon), y pixel (lateral), value of lateral arm of "origin", lon value of "origin"
    ppilon = 30/1
    ppiweight = -30/100  # needs to be negative as higher weights are up and upper left is 0,0
    ppilat = -30/1  # needs to be negative as right which is positive is up
    print(ppilon)
    print(ppiweight)

    # heli = R44()
    # heli.set_weight("FR_seat", 200)
    # heli.set_weight("FR_bag",50)
    # heli.set_vol("Main_fuel",20)
    # heli.calculate_com()
    # info = heli.get_com()
    print(info)
    lon_x_pos = ((info['longitudinal_arm'] - pos1[3]) * ppilon) + pos1[0]
    weight_y_pos = ((info['weight'] - pos1[2]) * ppiweight) + pos1[1]
    lat_y_pos = ((info['lateral_arm']-pos3[2])*ppilat) + pos3[1]
    print(lon_x_pos, weight_y_pos)

    with Image.open("static/images/R44/wb.jpg") as im:
        # 76 347 1500lbs 91 in lon
        # 227 317 1600 95

        draw = ImageDraw.Draw(im)
        # the weight part of the drawing
        draw.ellipse([lon_x_pos - 3, weight_y_pos - 3, lon_x_pos + 3, weight_y_pos + 3], fill="red", outline="red",
                     width=1)
        # the lateral part of the drawing
        draw.ellipse([lon_x_pos - 3, lat_y_pos - 3, lon_x_pos + 3, lat_y_pos + 3], fill="red", outline="red",
                     width=1)

        # write to stdout
        im.save("static/images/R44/output.jpg")

if __name__ == "__main__":
    main()