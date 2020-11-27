var selectedRow = null

function metodosJS() {
    if (validar()) {
        var formData = obtenerDatos();
        if (selectedRow == null)
            añadirElemento(formData);
        else
            actualizarElementos(formData);
        limpearElementos();
    }
}

function obtenerDatos() {
    var formData = {};
    formData["id"] = document.getElementById("id").value;
    formData["nombre"] = document.getElementById("nombre").value;
    formData["sexo"] = document.getElementById("sexo").value;
    formData["tel"] = document.getElementById("tel").value;
    formData["email"] = document.getElementById("email").value;
    formData["carrera"] = document.getElementById("carrera").value;
    formData["status"] = document.getElementById("status").value;
    formData["tipo"] = document.getElementById("tipo").value;
    return formData;
}

function añadirElemento(data) {
    var table = document.getElementById("altaUsuarios").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.id;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.nombre;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.sexo;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.tel;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.email;
    cell6 = newRow.insertCell(5);
    cell6.innerHTML = data.carrera;
    cell7 = newRow.insertCell(6);
    cell7.innerHTML = data.status;
    cell8 = newRow.insertCell(7);
    cell8.innerHTML = data.tipo;
    cell8 = newRow.insertCell(8);
    cell8.innerHTML = `<a onClick="editarElementos(this)">Editar</a>,
                        <a onClick="Eliminar(this)">Eliminar</a>`;
}

function limpearElementos() {
    document.getElementById("id").value = "";
    document.getElementById("nombre").value = "";
    document.getElementById("sexo").value = "";
    document.getElementById("tel").value = "";
    document.getElementById("email").value = "";
    document.getElementById("carrera").value = "--------------Seleccionar--------------";
    document.getElementById("status").value = "";
    document.getElementById("tipo").value = "";
    selectedRow = null;
}

function editarElementos(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("id").value = selectedRow.cells[0].innerHTML;
    document.getElementById("nombre").value = selectedRow.cells[1].innerHTML;
    document.getElementById("sexo").value = selectedRow.cells[2].innerHTML;
    document.getElementById("tel").value = selectedRow.cells[3].innerHTML;
    document.getElementById("email").value = selectedRow.cells[4].innerHTML;
    document.getElementById("carrera").value = selectedRow.cells[5].innerHTML;
    document.getElementById("status").value = selectedRow.cells[6].innerHTML;
    document.getElementById("tipo").value = selectedRow.cells[7].innerHTML;
}

function actualizarElementos(formData) {
    selectedRow.cells[0].innerHTML = formData.id;
    selectedRow.cells[1].innerHTML = formData.nombre;
    selectedRow.cells[2].innerHTML = formData.sexo;
    selectedRow.cells[3].innerHTML = formData.tel;
    selectedRow.cells[4].innerHTML = formData.email;
    selectedRow.cells[5].innerHTML = formData.carrera;
    selectedRow.cells[6].innerHTML = formData.status;
    selectedRow.cells[7].innerHTML = formData.tipo;
}

function Eliminar(td) {
    if (confirm('Deseas eliminar al Alumno?')) {
        row = td.parentElement.parentElement;
        document.getElementById("altaUsuarios").deleteRow(row.rowIndex);
        actualizarElementos();
    }
}

function validar() { //SCRIPT ANTI (GESTION,CONTA,INDUSTRIAL,ETC) 
    isValid = true;
    if (document.getElementById("id").value == "") {
        isValid = false;
        alert('Error: (id) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }


    else {
        isValid = true;
        if (!document.getElementById("fullNameValidationError").classList.contains("hide"))
            document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;

}