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

$('#carouselExample').on('slide.bs.carousel', function (e) {

    /*

    CC 2.0 License Iatek LLC 2018
    Attribution required
    
    */

    var $e = $(e.relatedTarget);
    
    var idx = $e.index();
    console.log("IDX :  " + idx);
    
    var itemsPerSlide = 8;
    var totalItems = $('.carousel-item').length;
    
    if (idx >= totalItems-(itemsPerSlide-1)) {
        var it = itemsPerSlide - (totalItems - idx);
        for (var i=0; i<it; i++) {
            // append slides to end
            if (e.direction=="left") {
                $('.carousel-item').eq(i).appendTo('.carousel-inner');
            }
            else {
                $('.carousel-item').eq(0).appendTo('.carousel-inner');
            }
        }
    }
});