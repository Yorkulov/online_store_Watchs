this.window.addEventListener('DOMContentLoaded', function () {
    const myVideo = this.document.querySelector('.video');
    const button = this.document.querySelector('.play-video');

    myVideo.muted = false;

    button.addEventListener('click', function () {
        if(myVideo.paused)
        {
            myVideo.play();
            button.innerHTML = "Pause Video";
        }
        else
        {
            myVideo.pause();
            button.innerHTML = "Play Video";
        }
    })
})