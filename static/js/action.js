var animateLeft = anime({
  targets: '.square',
  left: '50%',
  autoplay: false
});


var animateBackground = anime({
  targets: '.square',
  backgroundColor: '#f96',
  autoplay: false
});

var animateRadius = anime({
  targets: '.square',
  borderRadius: '50%',
  autoplay: false
});

var animateAll = anime({
  targets: '.square',
  backgroundColor: '#f96',
  borderRadius: '50%',
  left: '50%',
  autoplay: false
});

document.querySelector('.play-left').onclick = animateLeft.restart;

document.querySelector('.play-background').onclick = animateBackground.restart;

document.querySelector('.play-radius').onclick = animateRadius.restart;

document.querySelector('.play-all').onclick = animateAll.restart;
