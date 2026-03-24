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
    const currentIndex = element.dataset.ratingValue;
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

function lightUpStars(stars, upUntil)
{
    for (let i = 0; i < starCount; i++)
    {
        console.log("Original src: " + stars[i].src);    
        stars[i].src = emptyStarImage;
        console.log("Updated src: "  + stars[i].src);  
    }

    for (let i = 0; i < upUntil; i++)
    {
        console.log("Original src: " + stars[i].src);  
        stars[i].src = fullStarImage;
        console.log("Updated src: "  + stars[i].src);  
    }
}