function prepare_data(hueb) {
            let color = hueb.color;
            if (!color) {
                color = "#f1dcc9";
            }
            let colorF = document.getElementById("color-sender");
            colorF.value = color;

        }

let colorSender = document.getElementById("write-idea-form");
colorSender.addEventListener("submit", ()=>{
    prepare_data(hueb);
})
