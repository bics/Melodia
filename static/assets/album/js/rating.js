const goldStars = document.querySelectorAll('.gold-star');
const starCount = 5;
const emptyStarImage = "/static/assets/images/rating_star_gray.png";
const fullStarImage = "/static/assets/images/rating_star_full_transbg.png";

// Tooltip retrieval generated using ChatGPT
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
[...tooltipTriggerList].forEach(el => new bootstrap.Tooltip(el));

goldStars.forEach(star => {
    star.addEventListener('mouseover', highlightRating);
    star.addEventListener('click', submitRating);
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

// Below 2 methods generated using ChatGPT
function submitRating(event) {
    const element = event.currentTarget;
    const row = element.closest('.rating-row');
    const tooltip = bootstrap.Tooltip.getInstance(row);    
    const trackId = element.dataset.trackId;
    const ratingValue = parseInt(element.dataset.ratingValue);

    fetch('/artist/rate-track/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({
            track_id: trackId,
            rating: ratingValue
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Saved:', data);
        row.setAttribute('data-bs-original-title', 'Rating saved!');
        tooltip.show();    
        setTimeout(() =>
        {
            tooltip.hide();
            row.setAttribute('data-bs-original-title', '');
        }, 1500);        
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function getCSRFToken() {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}