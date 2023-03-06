const myFunction = (e) => {
    
    let reviewNode = e.target;
    
    while (reviewNode.nodeName !== 'BODY') {
    
      if (reviewNode.classList.contains('item')) {
        Swal.fire({
            title: 'Do you want to save the changes?',
            showDenyButton: true,
            showCancelButton: true,
            confirmButtonText: 'Apoyo',
            denyButtonText: `Falta`,
            focusCancel: true,
          }).then((result) => {
            /* Read more about isConfirmed, isDenied below */
            if (result.isConfirmed) {
                //Swal.fire('Saved!', '', 'success');
                if (e.target.classList.add('bg-primary')) {
                    alert("ya existe apoyo")
                };
                return
                e.target.innerText = "SI";                
                e.target.classList.add('bg-primary');
                e.target.classList.remove('bg-danger');
            } else if (result.isDenied) {
                //Swal.fire('Saved!', '', 'success');
                e.target.innerText = "NO";  
                e.target.classList.add('bg-danger');
                e.target.classList.remove('bg-primary');
            }
        })
        break;
      }      
      reviewNode = reviewNode.parentNode;
    }      
  }
  
  document.body.addEventListener('click', myFunction, false);


/*var myElementToCheckIfClicksAreInsideOf = document.querySelector('.item');
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
*/
