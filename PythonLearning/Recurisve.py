path= [[1,'Mumbai','Delhi'],[1,'Delhi','Goa'],[1,'Goa','Mumbai'],[2,'Mumbai','Banglore'],[2,'Banglore','Chennai'],[3,'Mumbai','Pune']]
OldFlightNum=0
Oldsource=""
OldDestination=""
Completepath=""
Counter=0
FirstCOunter=0
NoofFLight=1
DictKeys={}

for hops in path:
    Counter+=1
    FirstCOunter+=1
    flightno,Source,Destination=hops
    print(flightno,Source,Destination)
    if flightno in DictKeys.keys():
        DictKeys[flightno]=DictKeys[flightno]+'-'+Destination
    else:
        DictKeys[flightno] = Source + '-' + Destination

print(DictKeys)