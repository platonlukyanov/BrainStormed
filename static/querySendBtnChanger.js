

// Send button to > if display too short
var mediaQuery = window.matchMedia('(max-width: 720px)')
if (mediaQuery.matches) {

    var wibtn = document.getElementById("write-idea-btn");
    wibtn.innerText = ">";
}