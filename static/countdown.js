var count = 12;
var countdownEl = document.getElementById('countdown');
countdownEl.innerText = "До перезагрузки страницы: "+count+" сек.";
interval = setInterval(()=>{
    count--;
    console.log(count);
    countdownEl.innerText = "До перезагрузки страницы: "+count+" сек.";
    if (count <= 0) {
        var form = document.getElementById('idea-form');
        if (!form.value){
            window.location.reload();
            clearInterval(interval);
        }
        else {
            count = 12;
            
        }
    }
}, 1000);
