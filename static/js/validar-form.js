var buttonUp = () => {    
    let nameValue = document.getElementById("validationCustom01").value;
    if (nameValue.length == 8){    
        const data = { dni: nameValue };
        fetch('/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data),
            })            
        .then((response) => response.json())
        .then((data) => {

            console.log(data);
            if (data.person == true){
                Swal.fire('Any fool can use a computer');
                Swal.fire({                   
                    icon: 'success',
                    title: 'Your work has been saved',
                    showConfirmButton: false,
                    timer: 1500
                  })
            }
            else {
                Swal.fire({                   
                    icon: 'error',
                    title: 'Your work has been saved',
                    showConfirmButton: false,
                    timer: 1500
                  })
            }
        })
        .catch((error) => {
            console.error(error);
        });

    }
}
