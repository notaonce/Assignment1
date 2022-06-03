play = (e) => {
  console.log(e);
    const audio = document.querySelector(`audio[data-press="${e.keyCode}"]`);
    const key = document.querySelector(`li[data-press="${e.keyCode}"]`);
  if(audio) {
    audio.play();
    key.classList.add("play");
  }
}

pause = (e)=>{
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`li[data-key = "${e.keyCode}"]`);
  if(audio){
    audio.currentTime = 0;
    audio.pause();
    key.classList.remove("play");
  }
}

window.addEventListener("keypress", play);
window.addEventListener("keyup", pause);