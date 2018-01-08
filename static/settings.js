(() => {
    const isoInput = document.getElementById("iso-input");
    const speedInput = document.getElementById("speed-input");

    isoInput.addEventListener("input", event => {
        document.getElementById("iso-label").innerHTML = event.target.value;
    });

    speedInput.addEventListener("input", event => {
        document.getElementById("speed-label").innerHTML = Math.round(event.target.value / 100000);
    }); 
})();
