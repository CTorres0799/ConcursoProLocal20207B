var selectedRow = null;

function metodosJS(){
    if(validar()){
        var formData = obtenerDatos();
        if(selectedRow == null)
           añadirElementos(formData);
        else
            actualizarElemento(formData);
        limpiarElementos();
    }
}

function obtenerDatos(){
    var formData = {};
    formData ["IdProRes"] = document.getElementById("IdProRes").value;
    formData ["IdProPues"] = document.getElementById("IdProPues").value;
    formData ["IdEquipos"] = document.getElementById("IdEquipos").value;
    formData ["NombreEquipo"] = document.getElementById("NombreEquipo").value;
    formData ["NoContro1"] = document.getElementById("NoContro1").value;
    formData ["NoContro2"] = document.getElementById("NoContro2").value;
    formData ["NoContro3"] = document.getElementById("NoContro3").value;
    formData ["IdDocente"] = document.getElementById("IdDocente").value;
    formData ["IdCategoria"] = document.getElementById("IdCategoria").value;
    return formData;
}

function añadirElementos(data){
    var table = document.getElementById("altaEquipos").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.IdProRes;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.IdProPues;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.IdEquipos;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.NombreEquipo;
    cell5 = newRow.insertCell(4);
    cell2.innerHTML = data.NoContro1;
    cell6 = newRow.insertCell(5);
    cell6.innerHTML = data.NoContro2;
    cell7 = newRow.insertCell(6);
    cell7.innerHTML = data.NoContro3;
    cell8 = newRow.insertCell(7);
    cell8.innerHTML = data.IdDocente;
    cell9 = newRow.insertCell(8);
    cell9.innerHTML = data.IdCategoria;
    cell9 = newRowRow.insertCell(9); 
    cell9.innerHTML = `<a onClick="editarElementos(this)">Editar</a>,
                        <a onClick="Eliminar(this)">Eliminar</a>`;

}

function limpiarElementos(){
    document.getElementById("IdProRes").value ="";
    document.getElementById("IdProPues").value ="";
    document.getElementById("IdEquipos").value ="";
    document.getElementById("NombreEquipo").value ="";
    document.getElementById("NoContro1").value ="";
    document.getElementById("NoContro2").value ="";
    document.getElementById("NoContro3").value ="";
    document.getElementById("IdDocente").value ="";
    document.getElementById("IdCategoria").value ="";
    selectedRow = null;

}

function editarElementos(td){
    selectedRow = td.parentElement.parentElement;
    document.getElementById("IdProRes").value = selectedRow.cells[0].innerHTML;
    document.getElementById("IdProPues").value = selectedRow.cells[1].innerHTML;
    document.getElementById("IdEquipos").value = selectedRow.cells[2].innerHTML;
    document.getElementById("NombreEquipo").value = selectedRow.cells[3].innerHTML;
    document.getElementById("NoContro1").value = selectedRow.cells[4].innerHTML;
    document.getElementById("NoContro2").value = selectedRow.cells[5].innerHTML;
    document.getElementById("NoContro3").value = selectedRow.cells[6].innerHTML;
    document.getElementById("IdDocente").value = selectedRow.cells[7].innerHTML;
    document.getElementById("IdCategoria").value = selectedRow.cells[8].innerHTML;
    
}

function actualizarElemento(formData){
    selectedRow.cells[0].innerHTML = formData.IdProRes;
    selectedRow.cells[1].innerHTML = formData.IdProPues;
    selectedRow.cells[2].innerHTML = formData.IdEquipos;
    selectedRow.cells[3].innerHTML = formData.NombreEquipo;
    selectedRow.cells[4].innerHTML = formData.NoContro1;
    selectedRow.cells[5].innerHTML = formData.NoContro2;
    selectedRow.cells[6].innerHTML = formData.NoContro3;
    selectedRow.cells[7].innerHTML = formData.IdDocente;
    selectedRow.cells[8].innerHTML = formData.IdCategoria;
}

function Eliminar(td){
    if(confirm('Desea eliminar al Equipo?')){
        row = td.parentElement.parentElement;
        document.getElementById("altaEquipos").deleteRow(row.rowIndex);
        actualizarElementos();
    }

}

function validar(){
    isValid = true;
    if(document.getElementById("Nombre").value == ""){
        isValid = false;
        alert('Error: (Nombre) vacio, por favor intentelo de nuevo');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    else{
        isValid = true;
        if(!document.getElementById("fullNameValidationError").classList.contains("hide"));
           document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;
}





