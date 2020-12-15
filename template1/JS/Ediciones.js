var selectedRow = null;

function metodosJS(){
    if(validar()){
        var formDate = obtenerDatos();
        if(selectedRow == null)
        añadirElementos(formData);
    else
        actualizarElementos(formDate);
    limpiarElementos();
    }
}

function obtenerDatos(){
    var formData = {};
    formData ["IdEdicion"] = document.getElementById("IdEdicion").value;
    formData ["IdProPue"] = document.getElementById("IdProPue").value;
    formData ["IdProRes"] = document.getElementById("IdProRes").value;
    formData ["Nombre"] = document.getElementById("Nombre").value;
    formData ["FechaRegistro"] = document.getElementById("FechaRegistro").value;
    formData ["FechaEvento"] = document.getElementById("FechaEvento").value;
    return formData;
}

function añadirElementos(data){
    var table = document.getElementById("altaEdiciones").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.IdEdicion;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.IdProPue;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.IdProRes;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.Nombre;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.FechaRegistro;
    cell6 = newRow.insertCell(5);
    cell6.innerHTML = data.FechaEvento;
    cell6 = newRowRow.insertCell(6); 
    cell6.innerHTML = `<a onClick="editarElementos(this)">Editar</a>,
                        <a onClick="Eliminar(this)">Eliminar</a>`;

}

function limpiarElementos(){
    document.getElementById("IdEdicion").value ="";
    document.getElementById("IdProPue").value ="";
    document.getElementById("IdProRes").value ="";
    document.getElementById("Nombre").value ="";
    document.getElementById("FechaRegistro").value ="";
    document.getElementById("FechaEvento").value ="";
    selectedRow = null;

}

function editarElementos(td){
    selectedRow = td.parentElement.parentElement;
    document.getElementById("IdEdicion").value = selectedRow.cells[0].innerHTML;
    document.getElementById("IdProPue").value = selectedRow.cells[1].innerHTML;
    document.getElementById("IdProRes").value = selectedRow.cells[2].innerHTML;
    document.getElementById("Nombre").value = selectedRow.cells[3].innerHTML;
    document.getElementById("FechaRegistro").value = selectedRow.cells[4].innerHTML;
    document.getElementById("FechaEvento").value = selectedRow.cells[5].innerHTML;

}

function actualizarElementos(formData){
    selectedRow.cells[0].innerHTML = formData.IdEdicion;
    selectedRow.cells[1].innerHTML = formData.IdProPue;
    selectedRow.cells[2].innerHTML = formData.IdProRes;
    selectedRow.cells[3].innerHTML = formData.Nombre;
    selectedRow.cells[4].innerHTML = formData.FechaRegistro;
    selectedRow.cells[5].innerHTML = formData.FechaRegistro;
}

function Eliminar(td){
    if(confirm('Desea eliminar la Edición')){
       row = td.parentElement.parentElement;
       document.getElementById("altaEdicion").deleteRow(row.rowIndex);
       actualizarElementos(); 
    }
}


function validar(){
    isValid = true;
    if(document.getElementById("IdEdicion").value == ""){
        isValid = false;
        alert('Error: (IdEdicion) vacio, porfavor intentalo de nuevo');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    else{
        isValid = true;
        if(!document.getElementById("fullNameValidationError").classList.contains("hide"))
           document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;
}







