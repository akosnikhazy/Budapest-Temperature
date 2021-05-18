# visualizing Budapest's historical temperature data
# created by Ákos Nikházy

# dependencies: csv, PIL, matplotlib, numpy

# csv file explained:
# date;d_ta;d_tx;d_tn;d_rs;d_rf;d_ss;d_ssr

# d_ta	daily average temperature [°C]
# d_tx	daily max temperature [°C]
# d_tn	daily min temperature [°C]

# d_rs	daily rainfall [mm]
# d_rf	daily rainfall type
# d_ss	daylight [hours]
# d_ssr	global radiation [J/cm2]

# source: https://www.met.hu/eghajlat/magyarorszag_eghajlata/eghajlati_adatsorok/Budapest/adatok/napi_adatok/index.php


import csv
from PIL import Image, ImageDraw
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# the temperature value in question
# avarage 1
# max 2
# min 3
what = 2

img = Image.new('RGB', (1464, 476), (244, 244, 244))
draw = ImageDraw.Draw(img)

x1 = 0
y1 = 0
x2 = 4
y2 = 4

lastyear = "1901"

# source: https://stackoverflow.com/a/50784012/559110
def colorFader(c1, c2, mix=0):  # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1 = np.array(mpl.colors.to_rgb(c1))
    c2 = np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1 - mix) * c1 + mix * c2)


def normalize(val, m, mx):
    return (val - m) / (mx - m)


minv = 60.0  # bogus min value to calculate real one
maxv = -100  # bogus max value to calculate real one

with open('budapest-dataset.csv', newline='') as csvfile:
    csvr = csv.reader(csvfile, delimiter=';', quotechar='|')

    for row in csvr:
        if float(row[what]) < minv:
            minv = float(row[what])

        if float(row[what]) > maxv:
            maxv = float(row[what])

    csvfile.seek(0)

    for row in csvr:
        year = row[0].split('-')

        if year[0] != lastyear:
            lastyear = year[0]
            y1 = y1 + 4
            y2 = y2 + 4
            x1 = 0
            x2 = 4

        c = colorFader("#0000aa", "#aa0000", normalize(float(row[what]), minv, maxv))

        draw.rectangle(
            (x1, y1, x2, y2),
            fill=c)

        x1 = x1 + 4
        x2 = x2 + 4


img.save("images\\otherimage" + str(what) + ".png")
