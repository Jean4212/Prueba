document.getElementById("btn-close").addEventListener("click", function(event) {
    fetch('/logout')
    .then(response => {
        console.log(response)
    }) 
});