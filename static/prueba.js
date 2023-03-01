function ValidaDatos() {
    

    let url

    return

    const dni = document.getElementById("dni");
    const paterno = document.getElementById("paterno");
    const materno = document.getElementById("materno");
    const nombre = document.getElementById("nombre");
    const nacimiento = document.getElementById("nacimiento");

    if (!dni.value){alert("registre el dni"); dni.focus(); return};
    if (dni.value.length < 8){alert("DNI SON 8 DIGITOS"); dni.focus(); return};
    if (!paterno.value){alert("registre el apellido paterno"); paterno.focus(); return};
    if (paterno.value.length < 3){alert("paterno debe ser mayor a 3 DIGITOS"); paterno.focus(); return};
    if (!materno.value){alert("registre el apellido materno"); materno.focus(); return};
    if (materno.value.length < 3){alert("materno debe ser mayor a 3 DIGITOS"); materno.focus(); return};
    if (!nombre.value){alert("registre el nombre"); nombre.focus(); return};
    if (nombre.value.length < 3){alert("nombre debe ser mayor a 3 DIGITOS"); nombre.focus(); return};
    if (!nacimiento.value){alert("registre la fecha de nacimiento"); nacimiento.focus(); return};    
    if (parseInt(nacimiento.value.slice(0,4)) < 1950 || parseInt(nacimiento.value.slice(0,4)) > 2050){alert("fecha fuera de rango"); nacimiento.focus(); return};
    
    const data = {dni: dni.value, paterno:paterno.value, materno:materno.value, nombre:nombre.value, nacimiento:nacimiento.value};
    
    console.log(data);

    return

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

    
};

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
};


function ValidaNumeros(event) {
    let key = event.keyCode;
    if (key < 48 || key > 57){
        event.returnValue = false;
    };      
};

function ValidaLetras(event) {    
    let key = event.keyCode;
    if ((key < 65 || key > 90) && (key < 97 || key > 122) && (key < 241 || key > 241) && (key < 209 || key > 209) && (key < 32 || key > 32)){
        event.returnValue = false;   
    };                   
};

function ValidaAlpha(event) {
    let key = event.keyCode;    
    if ((key < 48 || key > 57) && (key < 65 || key > 90) && (key < 97 || key > 122)){
        event.returnValue = false;
    };                   
};

function ValidaFloat(event) {
    let key = event.keyCode;
    if ((key < 48 || key > 57) && (key < 46 || key > 46)){
        event.returnValue = false;
    };         
};

function Checked1(event) {
    if (event.srcElement.checked){        
        document.getElementById("ingreso").disabled = false;
        document.getElementById("planilla").disabled = false; 
        document.getElementById("movilidad").disabled = false; 
        document.getElementById("asignacion").disabled = false; 
        document.getElementById("aportacion").disabled = false; 
        document.getElementById("comision").disabled = false; 
    }else{
        document.getElementById("ingreso").value = "";
        document.getElementById("ingreso").disabled = true; 
        document.getElementById("planilla").value = "";
        document.getElementById("planilla").disabled = true; 
        document.getElementById("movilidad").value = "";
        document.getElementById("movilidad").disabled = true; 
        document.getElementById("asignacion").value = "";
        document.getElementById("asignacion").disabled = true; 
        document.getElementById("aportacion").value = "";
        document.getElementById("aportacion").disabled = true; 
        document.getElementById("comision").value = "";
        document.getElementById("comision").disabled = true; 
    };   
};

function Checked2(event) {
    if (event.srcElement.checked){
        document.getElementById("cuenta").disabled = false;
        document.getElementById("cargo").disabled = false; 
        document.getElementById("distrito").disabled = false; 
        document.getElementById("domicilio").disabled = false; 
        document.getElementById("area").disabled = false; 
        document.getElementById("cuspp").disabled = false; 
        document.getElementById("celular").disabled = false; 
        document.getElementById("licencia").disabled = false; 
        document.getElementById("categoria").disabled = false; 
        document.getElementById("revalidacion").disabled = false; 
        document.getElementById("file-foto").disabled = false; 
        document.getElementById("file-dni").disabled = false; 
        document.getElementById("file-licencia").disabled = false; 
        document.getElementById("file-policial").disabled = false; 
    }else{     
        document.getElementById("cuenta").value = "";
        document.getElementById("cuenta").disabled = true;
        document.getElementById("cargo").value = "";
        document.getElementById("cargo").disabled = true; 
        document.getElementById("distrito").value = "";
        document.getElementById("distrito").disabled = true; 
        document.getElementById("domicilio").value = "";
        document.getElementById("domicilio").disabled = true; 
        document.getElementById("area").value = "";
        document.getElementById("area").disabled = true; 
        document.getElementById("cuspp").value = "";
        document.getElementById("cuspp").disabled = true; 
        document.getElementById("celular").value = "";
        document.getElementById("celular").disabled = true; 
        document.getElementById("licencia").value = "";
        document.getElementById("licencia").disabled = true; 
        document.getElementById("categoria").value = "";
        document.getElementById("categoria").disabled = true; 
        document.getElementById("revalidacion").value = "";
        document.getElementById("revalidacion").disabled = true; 
        document.getElementById("file-foto").value = "";
        document.getElementById("file-foto").disabled = true; 
        document.getElementById("file-dni").value = "";
        document.getElementById("file-dni").disabled = true; 
        document.getElementById("file-licencia").value = "";
        document.getElementById("file-licencia").disabled = true; 
        document.getElementById("file-policial").value = "";
        document.getElementById("file-policial").disabled = true; 
    };   
};