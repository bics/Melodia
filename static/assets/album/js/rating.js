const goldStars = document.querySelectorAll('.gold-star');
const starCount = 5;
const emptyStarImage = "/static/assets/images/rating_star_gray.png";
const fullStarImage = "/static/assets/images/rating_star_full_transbg.png";

goldStars.forEach(star => {
    star.addEventListener('mouseover', highlightRating);
});

function highlightRating(event)
{
    const element = event.currentTarget;
    const currentTrack = element.dataset.trackId;
    const currentIndex = parseInt(element.dataset.ratingValue);
    const currentStars = getAllTrackStars(currentTrack)
    if (currentStars)
    {
        lightUpStars(currentStars, currentIndex);
    }
}

function getAllTrackStars(currentID)
{
    let stars = [];
    goldStars.forEach(star => {
        if (star.dataset.trackId == currentID)
        {
            stars.push(star);
        }
    });
    return stars;
}

// Light up stars, first make all gray, then gold up until the one hovered
function lightUpStars(stars, upUntil)
{
    for (let i = 0; i < starCount; i++)
    { 
        stars[i].src = emptyStarImage;
    }

    for (let i = 0; i < upUntil; i++)
    {
        stars[i].src = fullStarImage;
    }
}