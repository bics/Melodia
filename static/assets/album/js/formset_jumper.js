
const startingIndex = 2;
const finalIndex = 12; 
const selectDivNames = "featured_artist_collapse-";

let currentTarget = startingIndex;

const plusButton = document.getElementById("add-track-form");
const minusButton = document.getElementById("remove-track-form");
const selectedArtistList = document.getElementById("selected-artists-list");

plusButton.addEventListener("click", () => updateTarget(true));
minusButton.addEventListener("click", () => updateTarget(false));

//TODO reset form when removed

function updateTarget(isIncrease)
{
    let adjustedTarget = currentTarget;
    if (isIncrease)
    {
        adjustedTarget++;
    }

    if (!isIncrease)
    {
        adjustedTarget--;
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
        plusButton.setAttribute("data-bs-target", "#track-" + currentTarget)

        if ((currentTarget - 1) < startingIndex)
        {
            minusButton.classList.add("disabled");
        }
        else
        {
            minusButton.classList.remove("disabled");
        }
        minusButton.setAttribute("data-bs-target", "#track-" + (currentTarget - 1))
    }
}

function isInBounds(targetCount)
{
    if (targetCount <= startingIndex && targetCount > (finalIndex+1))
    {
        return false
    }
    return true
}

function updateSelectedList()
{
    //const selectedOptions = selectedArtistList.
}