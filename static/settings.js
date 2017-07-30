(() => {
    const rangeInput = document.getElementById("iso");

    rangeInput.addEventListener("input", event => {
        document.getElementById("label").innerHTML = event.target.value;
    });
})();
