/* This script will generate a series of Random Tables 
for each location and display them with collasable blocks.*/


// import items.json
//import items in json format
const res = await fetch('../data/items.json')
items = await res.json();

/* TO-DO:

- for each location gather encounters according to tags
- calculate probability of encounter based on tags, day-time and other factors
- generate random table with d100 rangers for each encounter
- generate HTML table inside 

Problems:
- How can I create a complex object like a div block and a table?





