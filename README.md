# Budapest-Temperature
A small script to visualize Budapest's historical temperature data

I stumbled upon this dataset: https://www.met.hu/eghajlat/magyarorszag_eghajlata/eghajlati_adatsorok/Budapest/adatok/napi_adatok/index.php

So I decided to visualize the data. It turned out rather nice, but did not put too much brain power in it, so the code is lazy and the color ranges are not really scientific. For example green is the temperate that I enjoy :D 

But you get the idea.

Update: I uploaded the nicecolor.py too. The name is ironic as the result isn't nice. I was experimenting with dynamic color range for different temperatures, but it didn't turn out very nice, so I given up on it. But others might develop it further. The idea is it has no bias towards some temperature ranges. But gradient between two colors is just not really useful.

Update 2: created a combined script that combines main.py and nicecolor.py. This creates an interesting, less biased result, where there are color difference inside categories. For example I call green "warm" but warm moves between green and red in color.
