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
    formData["Punto"] = document.getElementById("Punto").value;
    formData["Tiempo"] = document.getElementById("Tiempo").value;
    formData["Descripcion"] = document.getElementById("Descripcion").value;
    return formData;
}

function añadirElemento(data) {
    var table = document.getElementById("BancoProblemas").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.id;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.nombre;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.Punto;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.Tiempo;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.Descripcion;
    cell5 = newRow.insertCell(5);
    cell5.innerHTML = `<a onClick="editarElementos(this)">Editar</a>,
                        <a onClick="Eliminar(this)">Eliminar</a>`;
}

function limpearElementos() {
    document.getElementById("id").value = "";
    document.getElementById("nombre").value = "";
    document.getElementById("Punto").value = "";
    document.getElementById("Tiempo").value = "";
    document.getElementById("Descripcion").value = "";
    selectedRow = null;
}

function editarElementos(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("id").value = selectedRow.cells[0].innerHTML;
    document.getElementById("nombre").value = selectedRow.cells[1].innerHTML;
    document.getElementById("Punto").value = selectedRow.cells[2].innerHTML;
    document.getElementById("Tiempo").value = selectedRow.cells[3].innerHTML;
    document.getElementById("Descripcion").value = selectedRow.cells[4].innerHTML;
}

function actualizarElementos(formData) {
    selectedRow.cells[0].innerHTML = formData.id;
    selectedRow.cells[1].innerHTML = formData.nombre;
    selectedRow.cells[2].innerHTML = formData.Punto;
    selectedRow.cells[3].innerHTML = formData.Tiempo;
    selectedRow.cells[4].innerHTML = formData.Descripcion;
}

function Eliminar(td) {
    if (confirm('¿Deseas eliminar el Problema?')) {
        row = td.parentElement.parentElement;
        document.getElementById("BancoProblemas").deleteRow(row.rowIndex);
        actualizarElementos();
    }
}

function validar() { 
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