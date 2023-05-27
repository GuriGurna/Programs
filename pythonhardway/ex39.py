# create a mapping of state to abbrevation 
states = {
    'oregon':'OR',
    'florida':'FL',
    'california':'CA',
    'new york':'NY',
    'michigan':'MI'
}

#create a basic set of states and some cities in them 
cities = {
    'CA':'san francisco',
    'MI':'detroit',
    'FL':'jacksonville'
}

#add some more cities 
cities['NY'] = 'new york'
cities['OR'] = 'portland'

#print out some cities
print('-'*10)
print("NY state has:",cities['NY'])
print("OR state has:",cities['OR'])

#print some states
print('-'*10)
print("michigan's abbreviation is:",states['michigan'])
print("florida's abbreviation is:",states['florida'])

#do it by using the state then cities dict
print('-'*10)
print("michigan has:",cities[states['michigan']])
print("florida has:",cities[states['florida']])

#print every state abbreviaiton
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state}  is abbreviated {abbrev}")
      
#print ever city in state 
print('-'*10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do the both at the same time
print("-"*10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviared for {abbrev}") 
    print(f"and has city {cities[abbrev]}")   

print('-'*10)
#safely get a abbreviation by state that might not be there 
state = states.get('texas')

if not state:
    print("sorry , no texas")

#get a city with a default value 
city = cities.get('TX','does not exist')
print(f"the city for the state 'TX' is :{city}")
