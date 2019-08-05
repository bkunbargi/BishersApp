$(document).ready(function(){


$('.post').css('display','none')
$('.tweet').css('display','none')


})



function openBig(evt, cityName) {
    // Declare all variables
    var i, persiproj, guidelinks;

    // Get all elements with class="tabcontent" and hide them
    persiproj = document.getElementsByClassName("persiproj");
    for (i = 0; i < persiproj.length; i++) {
        persiproj[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    guidelinks = document.getElementsByClassName("guidelinks");
    for (i = 0; i < guidelinks.length; i++) {
        guidelinks[i].className = guidelinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}


function openCity(evt, cityName) {
    console.log(evt,cityName)
    // Declare all variables
    var i, tabcontent, tablinks;
    console.log("Hello")

    console.log($('.search'))


    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

function hideContent(project,content){


  var project_elements = $(`.${project}`)
  var content_to_keep = $(`.${content}`)
  var elements_to_hide = [];

  for (element = 0; element < project_elements.length; element++) {

    $(project_elements[element]).hide();


}
 for(element = 0; element < content_to_keep.length; element ++){

   $(content_to_keep[element]).show();
 }





}
