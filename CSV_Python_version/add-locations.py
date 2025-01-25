import json
import csv 


#load old json

locations_filename = "locations-list.json"

# load locations from csv file
# I am assuming the following structure id, name, tag

input_csv_locations_file = open('locations_list.csv', mode='r')
csv_locations_reader = csv.DictReader(input_csv_locations_file)
csv_locations = list(csv_locations_reader)

# Import new locations into JSON tag_list


locations_dict = {
	"locations": [

	]
	}
id_counter = -1	 
for row in csv_locations:
	if int(row['id']) == id_counter:
		# same encounter, multiple tag
		# append tag to last encounter in the dictionary
		locations_dict['locations'][-1]['tags'].append(row['tag'])
	else:
		# new encounter
		locations_dict['locations'].append(
				{
			"id" : int(row['id']),
			"name": row['name'],
			"tags": [row['tag']]

		}

		)
		id_counter += 1 


output_file = open(locations_filename,'w')
json.dump(locations_dict,output_file,indent=2)




