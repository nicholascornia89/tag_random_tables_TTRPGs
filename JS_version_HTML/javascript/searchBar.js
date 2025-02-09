const itemsList = document.getElementById('itemsList');
const searchBar = document.getElementById('searchBar');
let concatItems = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filtereditems = concatItems.filter((item) => {
        
        return (
            item.name.toLowerCase().includes(searchString) ||
            item.description.toLowerCase().includes(searchString)
            
        );
    });
    displayItems(filtereditems);
});

const loadItems = async () => {
    try {
        const res = await fetch('./data/items.json');
        items = await res.json();

        concatItems = items.locations.concat(items.encounters)

        concatItems = concatItems.concat(items.tags)

        displayItems(concatItems);
    } catch (err) {
        console.error(err);
    }
};

const displayItems = (items) => {
    const htmlString = items
        .map((item) => {
            return `
            <li class="item">
                <h2>${item.name}</h2>
                <p>${item.description}</p>
                <img src="${item.image}"></img>
            </li>
        `;
        })
        .join('');
    itemsList.innerHTML = htmlString;
};

loadItems();
