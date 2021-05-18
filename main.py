# visualizing Budapest's historical temperature data
# created by Ákos Nikházy

# dependencies: csv, PIL

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

# the temperature value in question
# avarage 1
# max 2
# min 3
what = 2

# Image dimensions: 4*366, 4*119 so every day is 4*4 square.
img = Image.new('RGB', (1464, 476), (244, 244, 244))
draw = ImageDraw.Draw(img)

x1 = 0
y1 = 0
x2 = 4
y2 = 4

# dataset starts at 1901-01-01
lastyear = "1901"

minv = 60.0  # bogus min value to calculate real one
maxv = -100  # bogus max value to calculate real one

with open('budapest-dataset.csv', newline='') as csvfile:
        csvr = csv.reader(csvfile, delimiter=';', quotechar='|')

        # if you need to know the min and max values in given category
        # you might need this if you want to choose other coloring
        # numbers or even methods

        # for row in csvr:
        #    if float(row[what]) < minv:
        #        minv = float(row[what])

        #    if float(row[what]) > maxv:
        #        maxv = float(row[what])

        # csvfile.seek(0)
        # print(minv,maxv)

        for row in csvr:
            year = row[0].split('-')

            # step to the next row (year)
            if year[0] != lastyear:
                lastyear = year[0]
                y1 = y1+4
                y2 = y2+4
                x1 = 0
                x2 = 4

            # decide what temperature value corresponds with what color
            d = float(row[what])

            # This seems lazy. It is lazy. But does the job.
            if d <= 100:
               c = (255,0,0)

            if d <= 40:
               c = (255,60,60)

            if d <= 30:
               c = (255,117,117)

            if d <= 20:
               c = (119,255,117)

            if d <= 10:
               c = (117,255,241)

            if d <= 0:
               c = (117,160,255)

            if d <= -10:
               c = (45,30,252)

            draw.rectangle(
                (x1, y1, x2, y2),
                fill=c)

            # step to next column (day)
            x1 = x1+4
            x2 = x2+4


img.save("images\\image" + str(what) + ".png")