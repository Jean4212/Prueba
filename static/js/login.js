 
document.getElementById("btn").addEventListener("click", function(event) {
    const username = document.getElementById("floatingInput");
    const password = document.getElementById("floatingPassword");
    

    if (username.value && password.value) {       
               
        const credentials = {
            username: username.value,
            password: password.value
        }
        const auth = btoa(username.value + ':' + password.value);

        fetch('/login', {
            method: 'POST',       
            headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},    
            body: JSON.stringify(credentials),    
        })
        .then((respuesta) => respuesta.json())
        .then((data) => {
            if (data.token == username.value) {
                console.log("es el usuario "+ username.value);
                localStorage.setItem('token', data.token);
                // Redirigir a la ruta protegida, incluyendo el token de autenticación en la cabecera
                window.location.href = '/protected';
            }         
                
              
            
        });

    };
});
