import csv
import plotly.express as pl

rows = []

with open('anyname.csv', 'r') as f:
    reader = csv.reader(f)
    

    for i in reader:
        rows.append(i)

headers = rows[0]
planetInfo = rows[1:]

headers[0] = 'index'

planetCount = {}

for i in planetInfo:
    if planetCount.get(i[11]):
        planetCount[i[11]] += 1
    else:
        planetCount[i[11]] = 1

maxSolarSystem = max(planetCount, key=planetCount.get)

print(maxSolarSystem)

planetsInSolar = list(planetInfo)



for i in planetsInSolar:
    planetMass = i[3]
    planetRadius = i[7]
    
    if planetMass.lower() == 'unknown':
        planetsInSolar.remove(i)
        continue
    else:
        planetMassValue = planetMass.split(' ')[0]
        planetMassRef = planetMass.split(' ')[1]
        
        if planetMassRef == 'Jupiters':
            planetMassValue = float(planetMassValue) * 317.8
            
        i[3] = planetMassValue

    if planetRadius.lower() == 'unknown':
        planetsInSolar.remove(i)
        continue
    else:
        planetRadiusValue = planetRadius.split(' ')[0]
        planetRadiusRef = planetRadius.split(' ')[2]
        
        if planetRadiusRef == 'Jupiter':
            planetRadiusValue = float(planetRadiusValue) * 11.2
            
        i[7] = planetRadiusValue

planets = []
massOfPlanets = []
nameOfPlanets = []
radiusOfPlanets = []
gravityOfPlanets = []
for i in planetsInSolar:
    if maxSolarSystem == i[11]:
        planets.append(i)
for i in planets:
    massOfPlanets.append(i[3])
    radiusOfPlanets.append(i[7])
    nameOfPlanets.append(i[1])

for i, v in enumerate(nameOfPlanets):
    G = 6.674e-11
    gravity = (G * float(massOfPlanets[i]) * 5.972e+24)/((float(radiusOfPlanets[i]) * 6371000) * (float(radiusOfPlanets[i]) * 6371000))
    gravityOfPlanets.append(gravity)

graph = pl.scatter(x = radiusOfPlanets, y = massOfPlanets, size = gravityOfPlanets)
graph.show()



        

    

       
    