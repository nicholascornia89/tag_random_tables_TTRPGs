import json

#load old json

encounters_filename = "encounters-list.json"
encounters_file = open(encounters_filename,'r',encoding = 'utf-8')
old_encounters = json.load(encounters_file)

tags_filename = "tags-list.json"
tags_file = open(tags_filename,'r',encoding = 'utf-8')
old_tags = json.load(tags_file)



def value_lookup(dictionary,field,value):
	for i in range(len(dictionary)):
		if dictionary[i][field] == value:
			return True
	
	return False


#append new element to json file

print("This script will insert a new Encounter to the JSON list:")

new_data = {
	"id" : len(old_encounters["encounters"]),
	"name": "",
	"occurence_factor": 1,
	"tags": []

}


print("Encounter name:")
exit = False
while exit == False:
	new_name = input()
	if value_lookup(old_encounters["encounters"],"name",new_name) == True:
		print("An encounter with the same name is already present, choose another name or exit")
	else: 
		exit = True

new_data["name"] = new_name
print("Encounter name added correcly")

print("Encounter occurence factor (float):")
new_data["occurence_factor"] =  float(input())

# tags

exit = False
while exit == False:
	new_tag = str(input("Tag associated to encounter:"))
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

data = old_encounters
data["encounters"].append(new_data)

encounters_file.close()
tags_file.close()
output_file = open(encounters_filename,'w')
json.dump(data,output_file,indent=2)



