(() => {
    let forms = document.getElementsByTagName("form") || [];

    for (let i = 0; i < forms.length; i++) {
        forms[i].addEventListener("submit", () => {
            disableButtons();
        });
    }

    function disableButtons() {
        let buttons = document.getElementsByTagName("button") || [];
    
        if(buttons.length <= 0) {
            return;
        }
    
        for (let i= 0; i < buttons.length; i++) {
            buttons[i].setAttribute("disabled", "disabled");
        };
    };
})();
