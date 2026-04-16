
const startingIndex = 2;
const finalIndex = 12; 
//Naming convention for collapse and list below
const selectDivName = "featured_artist_collapse-";
const selectListDivName = "selected-artists-list-";

let currentTarget = startingIndex;
//List to actual elements (might be confusing)
let selectDivList = [];
let selectListDivList = [];

const plusButton = document.getElementById("add-track-form");
const minusButton = document.getElementById("remove-track-form");

//Get all select and list element
window.onload = getAllFeaturedElements;

plusButton.addEventListener("click", () => updateTarget(true));
minusButton.addEventListener("click", () => updateTarget(false));

//Logic for adding/removing forms
function updateTarget(isIncrease)
{
    let adjustedTarget = currentTarget;
    let removing = false;
    if (isIncrease)
    {
        adjustedTarget++;
    }

    if (!isIncrease)
    {
        adjustedTarget--;
        removing = true;
    }

    if (isInBounds(adjustedTarget))
    {
        currentTarget = adjustedTarget;
        if (currentTarget > finalIndex)
        {
            plusButton.classList.add("disabled");
        }
        else
        {
            plusButton.classList.remove("disabled");
        }
        plusButton.setAttribute("data-bs-target", "#track-" + currentTarget);

        if ((currentTarget - 1) < startingIndex)
        {
            minusButton.classList.add("disabled");
        }
        else
        {
            minusButton.classList.remove("disabled");
        }
        minusButton.setAttribute("data-bs-target", "#track-" + (currentTarget - 1));

        if (removing)
        {
            //Reset logic generated using ChatGPT
            const track = document.querySelector("#track-" + currentTarget);

            track.querySelectorAll("input, textarea, select").forEach(el =>
            {
                el.value = "";
            });
            track.querySelectorAll("select").forEach(select =>
            {
                Array.from(select.options).forEach(option => option.selected = false);
            });
        }
    }
}

function isInBounds(targetCount)
{
    if (targetCount <= startingIndex && targetCount > (finalIndex+1))
    {
        return false;
    }
    return true;
}

function updateSelectedList(index)
{
    //Extracting selected option partially generated using ChatGPT
    const select = selectDivList[index].querySelector("select");

    let selectedItems = [];

    select.querySelectorAll("option").forEach(option => {
        if (option.selected)
        {
            selectedItems.push(option);
        }
    });

    const selectList = selectListDivList[index];

    selectList.innerHTML = "";

    selectedItems.forEach(item =>
    {
        let liElement = document.createElement("li");
        const textNode = document.createTextNode("feat " + item.text);
        liElement.classList.add("list-group-item");
        liElement.classList.add("graphite-background");
        liElement.classList.add("color-platinum");
        liElement.appendChild(textNode);
        selectList.appendChild(liElement);
    });
}

//Get all featured elements + add listeners to them
function getAllFeaturedElements()
{
    for (let i = 0; i < finalIndex; i++)
    {
        selectDivList.push(document.getElementById(selectDivName + i));
        selectDivList[i].querySelector("select").addEventListener("change", () => updateSelectedList(i));
        selectListDivList.push(document.getElementById(selectListDivName + i));        
    }
}