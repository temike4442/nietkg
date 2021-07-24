function openModal(pk) {
  document.getElementById("myModal").style.display = "block";
  document.cookie = "pk="+pk;
  console.debug(pk);
}

// Close the Modal
function closeModal() {
  document.getElementById("myModal").style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
    if (document.getElementById("myModal").style.display == "block")
    {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;


    const timeValue =  setInterval(function() {
  document.getElementById("progress_story").value +=1;
  if (document.getElementById("progress_story").value==100)
  {
    clearInterval(timeValue);
    document.getElementById("progress_story").value = 0;
    document.getElementById("next").click();
  }
  },100);
}

}