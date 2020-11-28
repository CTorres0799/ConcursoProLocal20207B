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
    formData["globo"] = document.getElementById("globo").value;
    formData["idProblemaPropuesto"] = document.getElementById("idProblemaPropuesto").value;
    formData["idEdicion"] = document.getElementById("idEdicion").value;
    formData["idCategoria"] = document.getElementById("idCategoria").value;
    formData["idProblema"] = document.getElementById("idProblema").value;
    return formData;
}

function añadirElemento(data) {
    var table = document.getElementById("altaPP").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.globo;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.idProblemaPropuesto;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.idEdicion;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.idCategoria;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.idProblema;
    cell5 = newRow.insertCell(5);
    cell5.innerHTML = `<a onClick="editarElementos(this)">Editar</a>
                       <a onClick="Eliminar(this)">Eliminar</a>`;
}

function limpearElementos() {
    document.getElementById("globo").value = "";
    document.getElementById("idProblemaPropuesto").value = "";
    document.getElementById("idEdicion").value = "";
    document.getElementById("idCategoria").value = "";
    document.getElementById("idProblema").value = "";
    selectedRow = null;
}

function editarElementos(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("globo").value = selectedRow.cells[0].innerHTML;
    document.getElementById("idProblemaPropuesto").value = selectedRow.cells[1].innerHTML;
    document.getElementById("idEdicion").value = selectedRow.cells[2].innerHTML;
    document.getElementById("idCategoria").value = selectedRow.cells[3].innerHTML;
    document.getElementById("idProblema").value = selectedRow.cells[4].innerHTML;
}

function actualizarElementos(formData) {
    selectedRow.cells[0].innerHTML = formData.globo;
    selectedRow.cells[1].innerHTML = formData.idProblemaPropuesto;
    selectedRow.cells[2].innerHTML = formData.idEdicion;
    selectedRow.cells[3].innerHTML = formData.idCategoria;
    selectedRow.cells[4].innerHTML = formData.idProblema;
}

function Eliminar(td) {
    if (confirm('Deseas eliminar el Problema Propuesto?:')) {
        row = td.parentElement.parentElement;
        document.getElementById("altaPP").deleteRow(row.rowIndex);
        actualizarElementos();
    }
}

function validar() { //SCRIPT ANTI (GESTION,CONTA,INDUSTRIAL,ETC) 
    isValid = true;
    if (document.getElementById("globo").value == "") {
        isValid = false;
        alert('Error: Campo (GLOBO) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    if (document.getElementById("idProblemaPropuesto").value == "") {
        isValid = false;
        alert('Error: Campo (idProblemaPropuesto) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    if (document.getElementById("idEdicion").value == "") {
        isValid = false;
        alert('Error: Campo (idEdicion) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    
    if (document.getElementById("idCategoria").value == "") {
        isValid = false;
        alert('Error: Campo (idCategoria) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    if (document.getElementById("idProblema").value == "") {
        isValid = false;
        alert('Error: Campo (idProblema) vacio, porfavor intentalo de nuevo :)');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }


    else {
        isValid = true;
        if (!document.getElementById("fullNameValidationError").classList.contains("hide"))
            document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;


}