var slideIndex = 0;
var src_list = [];
var caption_text = '';

function openModal(pk) {
  const cols = document.getElementById("columns");
  $.ajax({
    url: 'story/'+pk,
    type: 'get',
    success: function(response) {
        story_object = JSON.parse(response['story_object_list']);
        var story_object_items = JSON.parse(response['story_object_items_list']);
        caption_text = story_object[0]['fields']['story_title'];
        var str = '';
        var i = 0;
        story_object_items.forEach(item =>{
            var src = 'https://temike.pythonanywhere.com/media/'+item['fields']['story_src'];
            src_list.push(src);
            str +='<div class="column"><img class="demo" src="'+src+'" onclick="currentSlide('+i+')" style="width:100%"></div>';
            i++;
        });
        cols.innerHTML = str;
        var caption = document.getElementById("caption");
        caption.innerText = caption_text;
        document.getElementById("myModal").style.display = "block";
        showSlides(1,src_list);
        var story_items_fields = story_object_items[0]['fields'];
    },
    failure: function(data) {
        alert('Got an error ');
    }
});
}

// Close the Modal
function closeModal() {
  document.getElementById("myModal").style.display = "none";
  onChangeSlide();
  src_list = [];
}

function plusSlides(n) {
    onChangeSlide();
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  onChangeSlide();
  showSlides(slideIndex = n);
}

function onChangeSlide(){
    clearInterval(timeValue);
    document.getElementById("progress_story").value = 0;
}

function showSlides(n) {
    if (document.getElementById("myModal").style.display == "block")
    {
  var slider = document.getElementById("mySlides");
  var mySlideDiv = document.getElementById("mySlideDiv");
  var dots = document.getElementsByClassName("demo");
  if (n > src_list.length-1) {slideIndex = 0}
  if (n < 0) {slideIndex = src_list.length}
    slider.src = src_list[slideIndex];
    mySlideDiv.style.display = "block";
    timeValue =  setInterval(function() {
  document.getElementById("progress_story").value +=1;
  if (document.getElementById("progress_story").value==100)
  {
    onChangeSlide();
    document.getElementById("next").click();
  }
  },100);
}
}