document.getElementById("btn-close").addEventListener("click", function(event) {   
    fetch("/logout");  
    window.location.href = "/login";       
});
