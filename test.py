data = [["ID",'Zone','Stations'],
        ["1","Central Zone",'Station one, Station Two'],
        ["2","Central Zone 1",'Station one 1, Station Two 1'],
        ]

for row in data:
    for col in row:
        print(col,end='')