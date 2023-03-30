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

function EnviarDatos(datos) {
    fetch('/persons', {
        method: 'POST',       
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},    
        body: JSON.stringify(datos),    
    })            
    .then((respuesta) => respuesta.json())
    .then((resultado) => {     
        if (resultado.success) {
            const dni = datos.dni;
            resetearValores();
            document.getElementById("dni").focus();
            EnviarImgs(dni);            
        } else {
            console.log(resultado.success)
        }; 

    })
    .catch((error) => {
        console.log(error);
    });
};

function resetearValores() {
    const elementos = ["dni", "paterno", "materno", "nombre", "nacimiento", "ingreso", "planilla", "movilidad", "asignacion", "aportacion", "comision", "cuenta", "cargo", "distrito", "domicilio", "area", "cuspp", "celular", "licencia", "categoria", "revalidacion"];
    elementos.forEach((elemento) => {
        document.getElementById(elemento).value = "";
    });
};

function EnviarImgs(dni) {
    
    const newFormData = new FormData();
    const inputsId = ["file-foto", "file-dni", "file-licencia", "file-policial"];    
    let proceded = false;

    inputsId.forEach((id) => {       
        const input = document.getElementById(id);
        if (input.value) {
            const fileName = "${dni}-${id.split('-')[1]}.jpg";
            console.log("${dni} haha")

            newFormData.append("files", input.files[0], fileName);
            input.value = "";
            proceded = true;
        };
    });

    if (proceded) {
        fetch('/uploadfiles', {
            method: 'POST',        
            body: newFormData
        });
        Swal.fire({        
            icon: 'success',
            title: 'Los Datos Fueron Guardados',
            showConfirmButton: false,
            timer: 1200
        });
    };   
};

function validSwitch(event) {
    const ids = ["ingreso", "planilla", "movilidad", "asignacion", "aportacion", "comision", "cuenta", "cargo", "distrito", "domicilio", "area", "cuspp", "celular", "licencia", "categoria", "revalidacion", "file-foto", "file-dni", "file-licencia", "file-policial"];
      
    for (const id of ids) {
        const element = document.getElementById(id);
        if (event.srcElement.checked) {
            element.disabled = false;
        } else {
            element.value = "";
            element.disabled = true;
        }
    };
};

function validAportacion() {    
    const aportacion = document.getElementById("aportacion");
    const comision = document.getElementById("comision");
    if (!aportacion.value || aportacion.value == "onp"){        
        comision.value = null
    };
};

function validComision() {
    const aportacion = document.getElementById("aportacion");
    const comision = document.getElementById("comision");
    if (comision.value && (aportacion.value == "onp" || !aportacion.value)){        
        comision.value = null
        aportacion.focus();
    };
};