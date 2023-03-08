function ValidaDatos() {      
    const dni = document.getElementById("dni");
    const paterno = document.getElementById("paterno");
    const materno = document.getElementById("materno");
    const nombre = document.getElementById("nombre");
    const nacimiento = document.getElementById("nacimiento");

    if (!dni.value){Swal.fire({title:"Registra el DNI", didClose: () => {dni.focus()}}); return};
    if (dni.value.length < 8){Swal.fire({title:"Registra correctamente el DNI", didClose: () => {dni.focus()}}); return};
    if (!paterno.value){Swal.fire({title:"Registra el Apellido PATERNO", didClose: () => {paterno.focus()}}); return};
    if (paterno.value.length < 3){Swal.fire({title:"Registra correctamente el Apellido PATERNO", didClose: () => {paterno.focus()}}); return};
    if (!materno.value){Swal.fire({title:"Registra el Apellido MATERNO", didClose: () => {materno.focus()}}); return};
    if (materno.value.length < 3){Swal.fire({title:"Registra correctamente el Apellido MATERNO", didClose: () => {materno.focus()}}); return};
    if (!nombre.value){Swal.fire({title:"Registra el NOMBRE", didClose: () => {nombre.focus()}}); return};
    if (nombre.value.length < 3){Swal.fire({title:"Registra correctamente el NOMBRE", didClose: () => {nombre.focus()}}); return};
    if (!nacimiento.value){Swal.fire({title:"Registra la Fecha de NACIMIENTO", didClose: () => {nacimiento.focus()}}); return};
    let fechaNacimiento = parseInt(nacimiento.value.slice(0,4));
    if (fechaNacimiento < 1950 || fechaNacimiento > 2050){Swal.fire({title:"Registra correctamente la Fecha de NACIMIENTO", didClose: () => {nacimiento.focus()}}); return};
    
    const check1 = document.getElementById("Checked1");   

    if (!check1.checked){       
        const data = {dni: dni.value, paterno: paterno.value, materno: materno.value, nombre: nombre.value, nacimiento: nacimiento.value, ingreso: "", planilla: "", movilidad: "", asignacion: "", aportacion: "", comision: "", cuenta: "", cargo: "", distrito: "", domicilio: "", area: "", cuspp: "", celular: "", licencia: "", categoria: "", revalidacion: ""};
    
        EnviarDatos(data);    
        return    
    };
 
    const ingreso = document.getElementById("ingreso");
    const planilla = document.getElementById("planilla");
    const movilidad = document.getElementById("movilidad");
    const asignacion = document.getElementById("asignacion");
    const aportacion = document.getElementById("aportacion");
    const comision = document.getElementById("comision");

    if (!ingreso.value){Swal.fire({title:"Registra la Fecha de INGRESO", didClose: () => {ingreso.focus()}}); return};
    let fechaIngreso = parseInt(ingreso.value.slice(0,4));
    if (fechaIngreso < 1950 || fechaIngreso > 2050){Swal.fire({title:"Registra correctamente la Fecha de INGRESO", didClose: () => {ingreso.focus()}}); return};
    if (!planilla.value){Swal.fire({title:"Registra el Sueldo en PLANILLA", didClose: () => {planilla.focus()}}); return};
    if (aportacion.value && aportacion.value != "onp" && !comision.value){Swal.fire({title:"Registra el Tipo de COMISION", didClose: () => {comision.focus()}}); return};    
    
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
    fetch('/persons', {
        method: 'POST',       
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},    
        body: JSON.stringify(data),    
    })            
    .then((response) => response.json())
    .then((result) => {     
        if (result.success) {
            dni = data.dni          
            document.getElementById("dni").value = "";
            document.getElementById("paterno").value = "";
            document.getElementById("materno").value = "";
            document.getElementById("nombre").value = ""; 
            document.getElementById("nacimiento").value = "";
            document.getElementById("ingreso").value = "";
            document.getElementById("planilla").value = "";
            document.getElementById("movilidad").value = "";
            document.getElementById("asignacion").value = ""; 
            document.getElementById("aportacion").value = "";
            document.getElementById("comision").value = "";
            document.getElementById("cuenta").value = "";
            document.getElementById("cargo").value = "";
            document.getElementById("distrito").value = "";
            document.getElementById("domicilio").value = "";
            document.getElementById("area").value = "";
            document.getElementById("cuspp").value = "";
            document.getElementById("celular").value = "";
            document.getElementById("licencia").value = "";
            document.getElementById("categoria").value = "";
            document.getElementById("revalidacion").value = "";     
            document.getElementById("dni").focus();     
            EnviarImgs(dni);            
        };        
    })
    .catch((error) => {
        console.log(error);
    });
};

function EnviarImgs(dni) {
    const fileFoto = document.getElementById("file-foto");
    const fileDni = document.getElementById("file-dni");
    const fileLicencia = document.getElementById("file-licencia");
    const filePolicial = document.getElementById("file-policial");

    if (fileFoto.value || fileDni.value || fileLicencia.value || filePolicial.value) {
        const newFormData = new FormData();

        if (fileFoto.value){newFormData.append("files", fileFoto.files[0], dni + "-foto.jpg")};
        if (fileDni.value){newFormData.append("files", fileDni.files[0], dni + "-dni.jpg")};
        if (fileLicencia.value){newFormData.append("files", fileLicencia.files[0], dni + "-licencia.jpg")};
        if (filePolicial.value){newFormData.append("files", filePolicial.files[0], dni + "-policial.jpg")};

        fetch('/uploadfiles', {
            method: 'POST',        
            body: newFormData
        })
        .then(response => response.json())
        .then(result => {          
            if (result.success) {                
                document.getElementById("file-foto").value = "";
                document.getElementById("file-dni").value = ""; 
                document.getElementById("file-licencia").value = "";
                document.getElementById("file-policial").value = "";    
            }                       
        })
        .catch(err => {
            console.log(err);
        });
    }; 
    
    Swal.fire({        
        icon: 'success',
        title: 'Los Datos Fueron Guardados',
        showConfirmButton: false,
        timer: 1200
      });
};

function ComisionValid() {
    const aportacion = document.getElementById("aportacion");
    const comision = document.getElementById("comision");
    if (comision.value && (aportacion.value == "onp" || aportacion.value == "")){        
        comision.value = "";
        aportacion.focus();
    };
};

function AporteChange() {
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

    const ids = ["ingreso", "planilla", "movilidad", "asignacion", "aportacion", "comision", "cuenta", "cargo", "distrito", "domicilio", "area", "cuspp", "celular", "licencia", "categoria", "revalidacion", "file-foto", "file-dni", "file-licencia", "file-policial"];
      
    for (const id of ids) {
        const element = document.getElementById(id);
        if (event.srcElement.checked) {
            element.disabled = false;
        } else {
            element.value = "";
            element.disabled = true;
        }
    }
};