function hide(element) {
    console.log("hide called")
    element.style.opacity = "0.5"

}

function show(element) {
    console.log("show called")
    element.style.opacity = "1";
}

if (Number(window.screen.width.toString().replace("px")) > 780) {

    var el = document.getElementById("txtareahider");
    var form = document.getElementById("ifwrite");


    if (!cookie('statusIdeaForm')) {
        cookie.set('statusIdeaForm', 'opened', {
            path: window.location.pathname,
        });
    }

    if (cookie('statusIdeaForm') == "opened") {
        cookie.set('statusIdeaForm', 'closed', {
            path: window.location.pathname,
        });
        show(form);


    } else {

        cookie.set('statusIdeaForm', 'opened', {
            path: window.location.pathname,
        });
        hide(form);
    }


    el.addEventListener('click', () => {
        if (cookie('statusIdeaForm') == "opened") {
            cookie.set('statusIdeaForm', 'closed', {
                path: window.location.pathname,
            });

            hide(form);

        } else {

            cookie.set('statusIdeaForm', 'opened', {
                path: window.location.pathname,
            });
            show(form);
        }
    })
}