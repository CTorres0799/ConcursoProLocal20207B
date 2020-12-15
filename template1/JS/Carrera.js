var selectedRow = null;

function metodosJS(){
    if(validar()){
        var formData = obtenerDatos();
        if(selectedRow == null)
           añadirElementos(formData);
        else
            ActualizarElementos(formData);
        LimpearElementos();
    }
}
function obtenerDatos(){
    var formData = {};
    formData ["IdCarrera"] = document.getElementById("IdCarrera").value;
    formData ["NoControl"] = document.getElementById("NoControl").value;
    formData ["Carrera"] = document.getElementById("Carrera").value;
    formData ["Siglas"] = document.getElementById("Siglas").value;
    return formData;
}

function añadirElementos(data){
    var table = document.getElementById("altaCarrera").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.IdCarrera;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.NoControl;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.Carrera;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.Siglas;
    cell4 = newRowRow.insertCell(4); 
    cell4.innerHTML = `<a onClick="editarElementos(this)">Editar</a>,
                        <a onClick="Eliminar(this)">Eliminar</a>`;

}

function LimpearElementos(){
    document.getElementById("IdCarrera").value = "";
    document.getElementById("NoControl").value = "";
    document.getElementById("Carrera").value = "-----Selecciona la Carrera------";
    document.getElementById("Siglas").value = "-----Selecciona las Siglas de su Carrera-----";
    selectedRow = null;
}

function editarElementos(td){
    selectedRow = td.parentElement.parentElement;
    document.getElementById("IdCarrera").value = selectedRow.cells[0].innerHTML;
    document.getElementById("NoControl").value = selectedRow.cells[1].innerHTML;
    document.getElementById("Carrera").value = selectedRow.cells[2].innerHTML;
    document.getElementById("Siglas").value = selectedRow.cells[3].innerHTML;
}

function ActualizarElementos(formData){
    selectedRow.cells[0].innerHTML = formData.IdCarrera;
    selectedRow.cells[1].innerHTML = formData.NoControl;
    selectedRow.cells[2].innerHTML = formData.Carrera;
    selectedRow.cells[3].innerHTML = formData.Siglas;

}

function Eliminar(td){
    if(confirm('Seguro que desea eliminar la carrera?')){
        row = td.parentElement.parentElement;
        document.getElementById("altaCarrera").deleteRow(row.rowIndex);
        actualizarElementos();

    }
}

function validar(){
    isValid = true;
    if(document.getElementById("IdCarrera").value == ""){
        isValid  = false;
        alert('Error: (IdCarrera) vacio, Intentelo de nuevo Por Favor');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    else{
        isValid = true;
        if(!document.getElementById("fullNameValidationError").classList.contains("hide"))
           document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;
}

    


