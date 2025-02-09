//This script will modify or add new items to ../data/items.json

//import items in json format
const res = await fetch('../data/items.json')
items = await res.json();

/* TO DO 

- autocomplete and select from dropdown + new item option!
- button to add new tag
- button to sumbit change/ new item

/*