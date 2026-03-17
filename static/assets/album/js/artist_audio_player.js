
const mp3AudioPlayerSource = document.getElementById("mp3-audio-source")
const currentlyPlayingHeader = document.getElementById("currently-playing-header");
const nextPlayingHeader = document.getElementById("next-playing-header");
const play_buttons = document.querySelectorAll('.audio-control-button');

//Function partially generated using ChatGPT
play_buttons.forEach(button =>
{
    button.addEventListener('click', playTrack)
});

//<img class="audio-control-button" 
// id="audio-control-button-{{album.id}}-{{forloop.counter0}}" 
// src="{% static 'assets/images/play_button_small.png' %}" 
// alt="Play track button"
// data-track="{{ track.name }}" 
// data-track-position="{{ track.position }}">

function playTrack(event)
{
    const el = event.currentTarget;

    currentlyPlayingHeader.innerText = "Currently playing: " + el.dataset.track;
    nextPlayingHeader.innerHTML = "Next: " + getNextTrack(el.id);
}

function getNextTrack(currentIDString)
{
    const interData = currentIDString.split('-');
    const currentAlbumIndex = parseInt(interData[3]);
    const currentTrackIndex = parseInt(interData[4]);

    const nextTrackButton = document.getElementById("audio-control-button-" + currentAlbumIndex + "-" + (currentTrackIndex + 1));

    if (!nextTrackButton)
    {
        const firstTrackButton = document.getElementById("audio-control-button-" + currentAlbumIndex + "-0");
        return firstTrackButton.dataset.track;
    }

    return nextTrackButton.dataset.track;
}