import json

#load old json

tags_filename = "tags-list.json"
tags_file = open(tags_filename,'r',encoding = 'utf-8')
old_tags = json.load(tags_file)


def value_lookup(dictionary,field,value):
	for i in range(len(dictionary)):
		if dictionary[i][field] == value:
			return True
	
	return False


#append new element to json file

print("This script will insert a new Tag to the JSON list:")

new_data = {
	"id" : len(old_tags["tags"]),
	"name": "",
	"type": ""

}


print("Tag name:")
exit = False
while exit == False:
	new_name = input()
	if value_lookup(old_tags["tags"],"name",new_name) == True:
		print("A tag with the same name is already present, choose another name or exit")
	else: 
		exit = True

new_data["name"] = new_name
print("Tag name added correcly")

print("Tag type:")
new_data["type"] =  input()

# append new tag to the json list

data = old_tags
data["tags"].append(new_data)

tags_file.close()
output_file = open(tags_filename,'w')
json.dump(data,output_file,indent=2)



