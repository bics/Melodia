
const audioPlayer = document.getElementById("mp3-audio-source")
const play_buttons = document.querySelectorAll('.audio-control-button');

//Function generated using ChatGPT
play_buttons.forEach(button => {
  button.addEventListener('click', function (event) {
    const el = event.currentTarget; // or just "this"

    console.log(el.id);
    console.log(el.dataset.track);
    console.log(el.dataset.trackPosition);
  });
});