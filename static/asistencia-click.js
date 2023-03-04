var myElementToCheckIfClicksAreInsideOf = document.querySelector('.item');
// Listen for click events on body
document.body.addEventListener('click', function (event) {
    let id = event.target.id
    let elemento = document.getElementById(id);
    
    if (myElementToCheckIfClicksAreInsideOf.contains(event.target)) {
        console.log('clicked inside');
    } else {
        console.log('clicked outside');
    };
    return
    Swal.fire({
        title: "Registrar",      
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Apoyo',
        cancelButtonText: 'Falta'
    }).then((result) => {
              
        let validacion = result.isConfirmed
             
        if (validacion){
            if (elemento.style.backgroundColor == "blue"){
                elemento.style.backgroundColor = "";
            }else{
                elemento.style.backgroundColor = "blue";
            }
        }else{
            if (result.dismiss == "cancel"){
                if (elemento.style.backgroundColor == "red"){
                    elemento.style.backgroundColor = "";
                }else{
                    elemento.style.backgroundColor = "red";
                }
            }
        }
    });    
});

