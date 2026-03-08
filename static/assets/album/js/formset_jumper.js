
const startingIndex = 2;
const finalIndex = 12; 

const plusButton = document.getElementById("add-track-form");
const minusButton = document.getElementById("remove-track-form");

plusButton.addEventListener("click", () => updateTarget(true));
minusButton.addEventListener("click", () => updateTarget(false));


function updateTarget(isIncrease)
{
    if (isIncrease)
    {
        const targetAttribute = plusButton.getAttribute("data-bs-target").split('-');
        let targetCount = increaseTargetCount(parseInt(targetAttribute[1]))
        if (isInBounds(targetCount))
        {
            plusButton.setAttribute("data-bs-target", "#track-"+targetCount)
        }
    }

    if (!isIncrease)
    {
        const targetAttribute = minusButton.getAttribute("data-bs-target").split('-');
        let targetCount = increaseTargetCount(parseInt(targetAttribute[1]))
        if (isInBounds(targetCount))
        {
            minusButton.setAttribute("data-bs-target", "#track-"+targetCount)
        }
    }
}

function decreaseTargetCount(targetCount)
{
    targetCount--;
    return targetCount;
}

function increaseTargetCount(targetCount)
{    
    targetCount++;
    return targetCount;
}

function isInBounds(targetCount)
{
    if (targetCount >= startingIndex && targetCount <= finalIndex)
    {
        return true
    }
    return false
}