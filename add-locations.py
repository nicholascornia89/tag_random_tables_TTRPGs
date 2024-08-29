import json

#load old json

locations_filename = "locations-list.json"
locations_file = open(locations_filename,'r',encoding = 'utf-8')
old_locations = json.load(locations_file)

tags_filename = "tags-list.json"
tags_file = open(tags_filename,'r',encoding = 'utf-8')
old_tags = json.load(tags_file)


def value_lookup(dictionary,field,value):
	for i in range(len(dictionary)):
		if dictionary[i][field] == value:
			return True
	
	return False


#append new element to json file

print("This script will insert a new Location to the JSON list:")

new_data = {
	"id" : len(old_locations["locations"]),
	"name": "",
	"tags": []

}


print("Location name:")
exit = False
while exit == False:
	new_name = input()
	if value_lookup(old_locations["locations"],"name",new_name) == True:
		print("A location with the same name is already present, choose another name or exit")
	else: 
		exit = True

new_data["name"] = new_name
print("Location name added correcly")

# tags

exit = False
while exit == False:
	new_tag = str(input("Tag associated to location:"))
	if value_lookup(old_tags["tags"],"name",new_tag) == False:
		print("No tag with this name is present in the JSON tag")
	else:
		new_data["tags"].append(new_tag)

	print("Would you like to add another tag? y/n")
	answer = input()
	if answer == "y":
		exit = False
	else:
		exit = True

# append new encounter to the json list

data = old_locations
data["locations"].append(new_data)

locations_file.close()
tags_file.close()
output_file = open(locations_filename,'w')
json.dump(data,output_file,indent=2)



