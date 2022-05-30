import csv
import pandas as pd

rows = []

with open('stars.csv', 'r') as f:
    csv_r = csv.reader(f)
    for i in csv_r:
        rows.append(i)

headers = rows[0]
stars_data = rows[1:]
headers[0] = 'Index'

star_data = []

for star in stars_data:
    if star[2] != '?': 
        star[2] = float(star[2].strip("\'"))*1.989e+30
    
    if star[3] != '?':
        star[3] = float(star[3].strip("\'"))*6.957e+8
    star_data.append(star)

star_data_gravity = []

for star in star_data:
    if star[2] != '?' and star[3] != '?':
        gravity = (6.674e-11 * float(star[2]))/(float(star[3])*float(star[3]))
    star.append(gravity)
    star_data_gravity.append(star)

name = []
distance = []
mass = []
radius = []
gravity = []

for i in star_data_gravity:
    name.append(i[0])
    distance.append(i[1])
    mass.append(i[2])
    radius.append(i[3])
    gravity.append(i[4])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)

df.to_csv('final2.csv')