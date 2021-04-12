function show_items() {
    var menu = document.getElementById("menu-content");
    menu.classList.remove("normal");
    menu.classList.add("mobile");
    var burger = document.getElementById('burger');
    burger.style.position = "fixed";
    burger.style.right = "3%";

    
}
function hide_items() {
    var menu = document.getElementById("menu-content");
    menu.classList.remove("mobile");
    menu.classList.add("normal");
}

var burger = document.getElementById('burger');
var stat = false;
burger.addEventListener('click', () => {
    
    if (stat) {
        hide_items();
        stat = false;
    }
    else if (!stat) {
        show_items();
        stat = true;
    }
})