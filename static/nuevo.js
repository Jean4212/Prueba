function probar() {
    const name = document.getElementById("username");
    const fileFoto = document.getElementById("file-foto");

    const newFormData = new FormData();

    newFormData.append("username", name.value);
    newFormData.append("files", fileFoto.files[0]);

    console.log(newFormData.get("username"));
    fetch('/upp', {     
        headers: {'accept': 'application/json', 'Content-Type': 'multipart/form-data'},      
        method: 'POST',        
        body: newFormData
    })
    .then(response => response.json())
    .then(result => {          
        console.log(result)               
    })
    .catch(err => {
        console.log(err);
    });

}

