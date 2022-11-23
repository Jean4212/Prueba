function mifun(){

    const user = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    let datos = {"user": user, "password": password};
    let datosJSON = JSON.stringify(datos);

    fetch('/', {
          method: "POST",         
          headers: {"Content-Type": "application/json"},
          body: datosJSON
    })
    .then(response => response.json())  // convertir a json
    .then(json => {
      if (json.message == false){
        document.getElementById("username").value = "";
        document.getElementById("password").value = "";
        console.log("no ingresastes");
    }
    else{
      console.log("ingresastes")
    }
    }
    )    //imprimir los datos en la consola
    .catch(err => console.log('Solicitud fallida', err)); // Capturar errores
  ;}