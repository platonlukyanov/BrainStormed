function hide_description() {
    var desc = document.querySelector(".storm-desc");
    desc.style.display = "none";


}

function show_description() {
    var desc = document.querySelector(".storm-desc");
    desc.style.display = "block";

}

var status = "closed";
var showhidebtn = document.querySelector("#show-hide-btn");
showhidebtn.addEventListener('click', () => {
    if (status == "closed") {

        status = "open";
        show_description();
    } else {

        status = "closed";
        hide_description()
    }
})