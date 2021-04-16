function prepare_data(hueb) {
            var color = hueb.color;
            if (!color) {
                color = "#f1dcc9";
            }
            var colorF = document.getElementById("color-sender");
            colorF.value = color;

        }

var colorSender = document.getElementById("write-idea-form");
colorSender.addEventListener("submit", ()=>{
    prepare_data(hueb);
})
