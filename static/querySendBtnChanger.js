

// Send button to > if display too short
const mediaQuery = window.matchMedia('(max-width: 720px)')
if (mediaQuery.matches) {

    let wibtn = document.getElementById("write-idea-btn");
    wibtn.innerText = ">";
}