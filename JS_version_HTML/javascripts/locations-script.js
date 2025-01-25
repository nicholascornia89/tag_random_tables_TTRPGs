document.addEventListener("DOMContentLoaded", function () {
    fetch('../data/locations-list.json')
        .then(response => response.json())
        .then(data => {
            const dataDisplay = document.getElementById("locationsDisplay");

            // Goin through all elements:
            for (i=0;i<data.length-1;i++){
                // Create table row
                const rowElement = document.createElement("tr");
                rowElement.setAttribute('id','item-'+i);

                // Create HTML elements to display the JSON data
                const nameElement = document.createElement("td");
                nameElement.textContent = data[i].name;

                const descriptionElement = document.createElement("td");
                descriptionElement.textContent = data[i].description;

                // Turn list of tags into pipe separated elements
                let tagsString = "";
                const tagsList = data[i].tags;
                for (let j=0;j<data[i].tags.length-1;j++){
                    let item = data[i].tags[j];
                    tagsString += item+" | ";
                }
                const tagsElement = document.createElement("td");
                tagsString = tagsString.substr(0,tagsString.length-2);

                tagsElement.textContent = tagsString;

                // Append the elements to the "dataDisplay" table
                dataDisplay.appendChild(rowElement);
                rowElement.appendChild(nameElement);
                rowElement.appendChild(descriptionElement);
                rowElement.appendChild(tagsElement);
            }
        })
        .catch(error => console.error("Error fetching JSON data:", error));
});

