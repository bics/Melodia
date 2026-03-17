
const mp3AudioPlayerSource = document.getElementById("mp3-audio-source")
const currentlyPlayingHeader = document.getElementById("currently-playing-header");
const play_buttons = document.querySelectorAll('.audio-control-button');

//Function partially generated using ChatGPT
play_buttons.forEach(button =>
{
    button.addEventListener('click', () => playTrack(event)
    )
});

function playTrack(event)
{
    const el = event.currentTarget;

    currentlyPlayingHeader.innerText = "Currently playing: " + el.dataset.track;
}