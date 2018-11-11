(() => {
    const isoInput = document.getElementById("iso-input");
    const speedInput = document.getElementById("speed-input");

    isoInput.addEventListener("input", event => {
        document.getElementById("iso-label").innerHTML = event.target.value;
    });

    speedInput.addEventListener("input", event => {
        const val = event.target.value;

        if(val === "0") {
            label = "Auto";
        } else {
            label = `${event.target.value / 1000000}s`;
        }

        document.getElementById("speed-label").innerHTML = label;
    }); 
})();
