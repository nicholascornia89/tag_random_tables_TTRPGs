import csv
import json

locations_filename = "locations-list.json"
encounters_filename = "encounters-list.json"
tags_filename = "tags-list.json"

def json2dict(json_filename):

	json_file = open(json_filename,'r',encoding = 'utf-8')
	dict_name = json.load(json_file)

	return dict_name

def total_probability_location(lT,E,day_time):
	# generate the denominator factor for each location
	#lT is a list of tags related to the location
	#E is the dictionary of encounters
	S = 0
	for i in range(len(E["encounters"])):
		for j in range(len(E["encounters"][i]["tags"])):
			# seach encounter tag in location tag list
			if E["encounters"][i]["tags"][j] in lT:
				#multiplicative bonus day_time
				if day_time in E["encounters"][i]["tags"]:
					S += 2*E["encounters"][i]["occurrence_factor"]
				else:
					S += E["encounters"][i]["occurrence_factor"]

	return S

def encounter_probability(lT,lS,e,day_time):
	# generate the probability for each encounter related to the given location
	#lT is a list of tags related to the location
	#lS is the total probability of the location
	# e is the given encounter
	s = 0 
	for i in range(len(e["tags"])):
		if e["tags"][i] in lT:
			#multiplicative bonus for day_time
			if day_time in e["tags"]:
				s += 2
			else:
				s += 1
	return s*e["occurrence_factor"]/lS




# import json files
locations = json2dict(locations_filename)
encounters = json2dict(encounters_filename)
tags = json2dict(tags_filename)

# generate random tables for each location

print("Insert Day-time tag for tables:")
day_time = input()

csv_baseline_filename = "./output_tables/random_table-"
lS = []
for i in range(len(locations["locations"])):
	#generate a list of total probabilities for each locations
	lT = locations["locations"][i]["tags"]
	lS.append(total_probability_location(lT,encounters,day_time))
	# generate list of encounters related to the location
	lE = []
	for j in range(len(encounters["encounters"])):
		p=encounter_probability(lT,lS[i],encounters["encounters"][j],day_time)
		# select only relevant encounters
		if p>0:
			lE.append([encounters["encounters"][j]["name"],p])

	# generate csv file for location
	csv_filename = csv_baseline_filename+locations["locations"][i]["name"]+"-"+day_time+".csv"
	csv_file = open(csv_filename,'w')
	csv_dictionary = {'random_tables':[]}
	# populate csv_dictionary
	last_integer = 1
	for i in range(len(lE)):
		p=lE[i][1]*100
		if p-int(p)>0.5:
			p=int(p)+1
		else:
			p=int(p)
		csv_dictionary["random_tables"].append({"name": lE[i][0], "results": str(last_integer)+"-"+str(last_integer+p-1) })
		last_integer = last_integer+p

	#adjust last value to 100
	if csv_dictionary["random_tables"][-1]['results'][-3:] == "100":
		break
	else:
		# no 100 as value
		if csv_dictionary["random_tables"][-1]['results'][-3:] == "101":
			csv_dictionary["random_tables"][-1]['results'] = csv_dictionary["random_tables"][-1]['results'].replace("101","100")
		else:
			csv_dictionary["random_tables"][-1]['results'] = csv_dictionary["random_tables"][-1]['results'].replace("99","100")

	# export csv_dictionary to csv table
	w = csv.writer(csv_file)
	w.writerow(csv_dictionary['random_tables'][0].keys())
	for i in csv_dictionary['random_tables']:
		w.writerow(i.values())









