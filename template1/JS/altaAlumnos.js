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
    formData["noControl"] = document.getElementById("noControl").value;
    formData["sel1"] = document.getElementById("sel1").value;
    formData["idProblemasResueltos"] = document.getElementById("idProblemasResueltos").value;
    formData["idCarrera"] = document.getElementById("idCarrera").value;
    formData["idUsuario"] = document.getElementById("idUsuario").value;
    return formData;
}

function añadirElemento(data) {
    var table = document.getElementById("altaAlumno").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.noControl;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.sel1;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.idProblemasResueltos;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.idCarrera;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.idUsuario;
    cell5 = newRow.insertCell(5);
    cell5.innerHTML = `<a onClick="editarElementos(this)">Editar</a>
                       <a onClick="Eliminar(this)">Eliminar</a>`;
}

function limpearElementos() {
    document.getElementById("noControl").value = "";
    document.getElementById("sel1").value = "------------Seleccionar------------";
    document.getElementById("idProblemasResueltos").value = "";
    document.getElementById("idCarrera").value = "";
    document.getElementById("idUsuario").value = "";
    selectedRow = null;
}

function editarElementos(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("noControl").value = selectedRow.cells[0].innerHTML;
    document.getElementById("sel1").value = selectedRow.cells[1].innerHTML;
    document.getElementById("idProblemasResueltos").value = selectedRow.cells[2].innerHTML;
    document.getElementById("idCarrera").value = selectedRow.cells[3].innerHTML;
    document.getElementById("idUsuario").value = selectedRow.cells[4].innerHTML;
}

function actualizarElementos(formData) {
    selectedRow.cells[0].innerHTML = formData.noControl;
    selectedRow.cells[1].innerHTML = formData.sel1;
    selectedRow.cells[2].innerHTML = formData.idProblemasResueltos;
    selectedRow.cells[3].innerHTML = formData.idCarrera;
    selectedRow.cells[4].innerHTML = formData.idUsuario;
}

function Eliminar(td) {
    if (confirm('Deseas eliminar al Alumno?')) {
        row = td.parentElement.parentElement;
        document.getElementById("altaAlumno").deleteRow(row.rowIndex);
        actualizarElementos();
    }
}

function validar() { //SCRIPT ANTI (GESTION,CONTA,INDUSTRIAL,ETC) 
    isValid = true;
    if (document.getElementById("noControl").value == "") {
        isValid = false;
        alert('Error: (No.Control) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    if (document.getElementById("idProblemasResueltos").value == "") {
        isValid = false;
        alert('Error: (idProblemasResueltos) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    
    if (document.getElementById("idCarrera").value == "") {
        isValid = false;
        alert('Error: (idCarrera) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    if (document.getElementById("idUsuario").value == "") {
        isValid = false;
        alert('Error: (idUsuario) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    else {
        isValid = true;
        if (!document.getElementById("fullNameValidationError").classList.contains("hide"))
            document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;


}
