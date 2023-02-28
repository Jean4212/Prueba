function hola() {
    
    const dni = document.getElementById("dni");
    const paterno = document.getElementById("paterno");
    const materno = document.getElementById("materno");
    const nombre = document.getElementById("nombre");
    const nacimiento = document.getElementById("nacimiento");

    if (!dni.value){alert("registre el dni"); dni.focus(); return};
    if (dni.value.length < 8){alert("DNI SON 8 DIGITOS"); dni.focus(); return};
    if (!paterno.value){alert("registre el apellido paterno"); paterno.focus(); return};
    if (!materno.value){alert("registre el apellido materno"); materno.focus(); return};
    if (!nombre.value){alert("registre el nombre"); nombre.focus(); return};
    if (!nacimiento.value){alert("registre la fecha de nacimiento"); nacimiento.focus(); return};
   
    const data = {dni: dni.value, paterno:paterno.value, materno:materno.value, nombre:nombre.value, nacimiento:nacimiento.value};
 
    fetch('/persons', {
        method: 'POST',       
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)       
    })            
    .then((response) => response.json())
    .then((data) => {
        console.log(data.message);           
    })
    .catch((error) => {
        console.error(error);
    });

    
}

function buscar_datos() {
   
    const dni = document.getElementById("change").value;

    if (dni.length == 8){
        fetch('/persons?dni=' + dni, {
            method: 'GET',       
            headers: {'Content-Type': 'application/json'}           
            })            
        .then((response) => response.json())
        .then((data) => {
            console.log(data);   
            document.getElementById("dni").value = data.dni;
            document.getElementById("paterno").value = data.paterno;
            document.getElementById("materno").value = data.materno;
            document.getElementById("nombre").value = data.nombre;
            document.getElementById("nacimiento").value = data.nacimiento;
            })
        .catch((error) => {
                console.log(error);
            });
    }
    else {
        document.getElementById("dni").value = "";
        document.getElementById("paterno").value = "";
        document.getElementById("materno").value = "";
        document.getElementById("nombre").value = "";
        document.getElementById("nacimiento").value = "";
    }    
}


function ValidaNumeros(event) {
    let key = event.keyCode;
    if (key < 48 || key > 57){
        event.returnValue = false;
    }         
}

function ValidaLetras(event) {    
    let key = event.keyCode;
    if ((key < 65 || key > 90) && (key < 97 || key > 122) && (key < 241 || key > 241) && (key < 209 || key > 209) && (key < 32 || key > 32)){
        event.returnValue = false;   
    }                   
}

function ValidaNumLet(event) {    
    let key = event.keyCode;
    if ((key < 65 || key > 90) && (key < 97 || key > 122) && (key < 241 || key > 241) && (key < 209 || key > 209) && (key < 32 || key > 32)){
        event.returnValue = false;   
    }                   
}   
  

