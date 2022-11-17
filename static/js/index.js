function myfunctionName(){

    const user = document.getElementById("typeEmailX-2").value;
    const password = document.getElementById("typePasswordX-2").value;

    let datos = {"user": user, "password": password};
    let datosJSON = JSON.stringify(datos);

    fetch('/user', {
          method: "POST",         
          headers: {"Content-Type": "application/json"},
          body: datosJSON
    })
    .then(response => response.json())  // convertir a json
    .then(json => console.log(json))    //imprimir los datos en la consola
    .catch(err => console.log('Solicitud fallida', err)); // Capturar errores
  ;}