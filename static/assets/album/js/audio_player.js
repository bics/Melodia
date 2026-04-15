
const audioPlayer = document.getElementById("audio-player");
const currentlyPlayingHeader = document.getElementById("currently-playing-header");
const nextPlayingHeader = document.getElementById("next-playing-header");
const play_buttons = document.querySelectorAll('.audio-control-button');
const audioPlayerDiv = document.getElementById("audio-player-div");

let currentlyPlayingNode;
let nextPlayingNode;

//Function partially generated using ChatGPT
//Attach click function for each play button
play_buttons.forEach(button =>
{
    button.addEventListener('click', playTrack)
});

audioPlayer.addEventListener("ended", playNextTrack);

//<img class="audio-control-button" 
// id="audio-control-button-{{album.id}}-{{forloop.counter0}}" 
// src="{% static 'assets/images/play_button_small.png' %}" 
// alt="Play track button"
// data-track="{{ track.name }}" 
// data-track-position="{{ track.position }}">

function playTrack(event)
{
    audioPlayerDiv.classList.remove("hidden");
    const element = event.currentTarget;
    currentlyPlayingNode = element;
    nextPlayingNode = getNextTrack(element.id);
    
    audioPlayer.src = element.dataset.trackUrl;
    audioPlayer.load();    
    audioPlayer.play();
    updateUI(element.dataset.track, nextPlayingNode.dataset.track);
}

function playNextTrack()
{
    if (nextPlayingNode)
    {
        audioPlayer.src = nextPlayingNode.dataset.trackUrl;
        audioPlayer.load();
        audioPlayer.play();
        currentlyPlayingNode = nextPlayingNode;
        nextPlayingNode = getNextTrack(currentlyPlayingNode.id);        
        updateUI(currentlyPlayingNode.dataset.track, nextPlayingNode.dataset.track);
    }
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
        return firstTrackButton;
    }

    return nextTrackButton;
}

function updateUI(currentlyPlayingTrack, nextPlayingTrack)
{
    currentlyPlayingHeader.innerText = "Currently playing: " + currentlyPlayingTrack;
    nextPlayingHeader.innerText = "Next: " + nextPlayingTrack;
}