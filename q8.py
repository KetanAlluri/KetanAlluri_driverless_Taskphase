import csv
import math
with open('cones.csv', mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    f=['coneid','x','y','colour']
    cones=[]
    for d in reader:
        x=int(d['x'])
        y=int(d['y'])
        l= math.sqrt((x*x)+(y*y))
        cones.append((l,d))
    cones.sort(key=lambda p:p[0])
    with open("blue.csv",mode='w',newline='',encoding='utf-8') as blue, \
            open("yellow.csv",mode='w',newline='',encoding='UTF-8') as yellow:
            bluew=csv.DictWriter(blue, fieldnames=f)
            bluew.writeheader()
            yelw=csv.DictWriter(yellow, fieldnames=f)
            yelw.writeheader()
            bluec=[]
            yellowc=[]
            for c in cones:
                row_dict=c[1]
                if row_dict['colour'].lower()=='blue':
                    bluew.writerow(row_dict)
                    bluec.append(row_dict)
                elif row_dict["colour"].lower()=='yellow':
                    yelw.writerow(row_dict)
                    yellowc.append(row_dict)
    with open('centreline.csv',mode='w',newline='',encoding='utf-8') as midpoint:
        centre=csv.writer(midpoint)
        centre.writerow(['x','y'])
        for c in bluec:
            bluex=int(c['x'])
            bluey=int(c['y'])
            sd=float('inf')
            nyx=0
            nyy=0
            for y in yellowc:
                yellowx=int(y['x'])
                yellowy=int(y['y'])
                dist=math.sqrt((bluex-yellowx)*(bluex-yellowx)+(bluey-yellowy)*(bluey-yellowy))
                if dist<sd:
                    sd=dist
                    nyx=yellowx
                    nyy=yellowy
                mx,my=(bluex+nyx)/2,(bluey+nyy)/2
            centre.writerow([mx,my])
                   


    
    