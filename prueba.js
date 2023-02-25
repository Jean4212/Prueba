var buttonUp = () => {    
    
    const data = { dni: "uno", paterno:"uno", materno:"uno", nombre:"uno", nacimiento:"uno"};
    fetch('http://localhost:8000/persons?dni=jeanq1', {
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

