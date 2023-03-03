function ValidaDatos(event) {   

    //const fileFoto = document.getElementById("file-foto");
    //const fileDni = document.getElementById("file-dni");
    //const fileLicencia = document.getElementById("file-licencia");
    //const filePolicial = document.getElementById("file-policial");
    
    //const files = new FormData();

    //if (fileFoto.value){files.append("file-foto", fileFoto.files[0])};
    //if (fileDni.value){files.append("file-dni", fileDni.files[0])};
    //if (fileLicencia.value){files.append("file-licencia", fileLicencia.files[0])};
    //if (filePolicial.value){files.append("file-policial", filePolicial.files[0])};

    let fileFoto = document.getElementById("file-foto");
    let fileDni = document.getElementById("file-dni");
    //let fileee2 = document.getElementById("file-dni")
    var xxx = new FormData();
    xxx.append("files1", fileFoto.files[0]);
    xxx.append("files2", fileDni.files[0]);

    
    //xxx.append("file2", fileee2.files[0]);
    fetch('/uploadfiles', {
        method: 'POST',        
        body: xxx
    })
    .then(res => res.json())
    .then(res => {
        console.log(res);                   
    })
    .catch(err => {
        console.log(err);
     });



    return

    let fileee = document.getElementById("file-foto")
    //let fileee2 = document.getElementById("file-dni")
    var xxx = new FormData();
    xxx.append("file", fileee.files[0]);
    //xxx.append("file2", fileee2.files[0]);
    fetch('/uploadfile', {
        method: 'POST',        
        body: xxx
    })
    .then(res => res.json())
    .then(res => {
        console.log(res);                   
    })
    .catch(err => {
        console.log(err);
     });


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
    let fechaNacimiento = parseInt(nacimiento.value.slice(0,4));
    if (fechaNacimiento < 1950 || fechaNacimiento > 2050){alert("fecha fuera de rango"); nacimiento.focus(); return};
    
    const check1 = document.getElementById("Checked1");   

    if (!check1.checked){       
        const data = {dni: dni.value, paterno: paterno.value, materno: materno.value, nombre: nombre.value, nacimiento: nacimiento.value, ingreso: "", planilla: "", movilidad: "", asignacion: "", aportacion: "", comision: "", cuenta: "", cargo: "", distrito: "", domicilio: "", area: "", cuspp: "", celular: "", licencia: "", categoria: "", revalidacion: ""};
    
        EnviarDatos(data);        
    };
 
    const ingreso = document.getElementById("ingreso");
    const planilla = document.getElementById("planilla");
    const movilidad = document.getElementById("movilidad");
    const asignacion = document.getElementById("asignacion");
    const aportacion = document.getElementById("aportacion");
    const comision = document.getElementById("comision");

    if (!ingreso.value){alert("registra la fecha de ingreso"); ingreso.focus(); return};
    let fechaIngreso = parseInt(ingreso.value.slice(0,4));
    if (fechaIngreso < 1950 || fechaIngreso > 2050){alert("fecha de ingreso fuera de rango"); ingreso.focus(); return};
    if (!planilla.value){alert("registre el sueldo en planilla"); planilla.focus(); return};  
    if (aportacion.value && aportacion.value != "onp" && !comision.value){alert("seleccione la comision"); comision.focus(); return};    
    
    const cuenta = document.getElementById("cuenta");
    const cargo = document.getElementById("cargo");
    const distrito = document.getElementById("distrito");
    const domicilio = document.getElementById("domicilio");
    const area = document.getElementById("area");
    const cuspp = document.getElementById("cuspp");
    const celular = document.getElementById("celular");
    const licencia = document.getElementById("licencia");
    const categoria = document.getElementById("categoria");
    const revalidacion = document.getElementById("revalidacion");

    const data = {dni: dni.value, paterno: paterno.value, materno: materno.value, nombre: nombre.value, nacimiento: nacimiento.value, ingreso: ingreso.value, planilla: planilla.value, movilidad: movilidad.value, asignacion: asignacion.value, aportacion: aportacion.value, comision: comision.value, cuenta: cuenta.value, cargo: cargo.value, distrito: distrito.value, domicilio: domicilio.value, area: area.value, cuspp: cuspp.value, celular: celular.value, licencia: licencia.value, categoria: categoria.value, revalidacion: revalidacion.value};
    
    EnviarDatos(data);        
};

function EnviarDatos(data) {
    
    /*const NewData = new FormData();    

    for (let key in data) {
        NewData.append(key, data[key]);
    };    
    const input = document.getElementById("file-foto");
    NewData.append("file-foto", input.files[0]);
    //console.log(NewData);
    //return
    */
    


    fetch('/persons', {
        method: 'POST',       
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},    
        body: JSON.stringify(data),    
    })            
    .then((response) => response.json())
    .then((data) => {
        
        console.log(data);
    })
    .catch((error) => {
        console.log(error);
    });
};

function ComisionValid(event) {
    const aportacion = document.getElementById("aportacion");
    const comision = document.getElementById("comision");
    if (comision.value && (aportacion.value == "onp" || aportacion.value == "")){        
        comision.value = "";
        aportacion.focus();
    };
};

function AporteChange(event) {
    const aportacion = document.getElementById("aportacion");
    const comision = document.getElementById("comision");
    if (!aportacion.value || aportacion.value == "onp"){        
        comision.value = ""
    };
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