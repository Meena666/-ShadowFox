aus=["Syndey","Melbourne","Brisbane","Perth"]
uae=["Dubai","Abu Dhabi","Sharjah","Ajman"]
ind=["Mumbai","Bangalore","Chennai","Delhi"]
x=input("Enter a city name:")
if x in aus:
    print(x,"is in Australia")
elif x in uae:
    print(x,"is in UAE")
else:
    print(x,"is in India")
    
