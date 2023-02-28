function hola(){

    const change = document.getElementById("change").value;
    const dni = document.getElementById("dni").value;
    const paterno = document.getElementById("paterno").value;
    const materno = document.getElementById("materno").value;
    const nombre = document.getElementById("nombre").value;
    const nacimiento = document.getElementById("nacimiento").value;

    const data = {dni: dni, paterno:paterno, materno:materno, nombre:nombre, nacimiento:nacimiento};

    console.log(data);

    fetch('/persons?dni=' + change, {
        method: 'PUT',       
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)       
        })            
    .then((response) => response.json())
    .then((data) => {
        console.log(data);           
        })
        .catch((error) => {
            console.error(error);
        });

    
}



function buscar_datos(){
   
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

