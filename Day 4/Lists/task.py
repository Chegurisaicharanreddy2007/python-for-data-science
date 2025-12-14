states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america)
print(states_of_america[2])
states_of_america[1]="xyz" #changing the el in list
print(states_of_america)
states_of_america.append("abcd")
print(states_of_america)
states_of_america.extend(["sai","saii"])
print(states_of_america)
states_of_america.insert(len(states_of_america)-1,"xuu")
print(states_of_america)
states_of_america.remove("New Jersey")
print(states_of_america)
print(states_of_america.pop(4))