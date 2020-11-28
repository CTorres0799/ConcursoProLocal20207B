var selectedRow = null

//VALIDACIONES
function validarNoControl(cad) {
    var patron = /\d{8}/;
    if (cad.length < 5) {
        return "El No.Control es de al menos 8 digitos";
    }
    else {
        if (cad.length <= 10) {
            if (!patron.test(cad)) {
                return 'La cedula solo debe incluir digitos <br>'
            }
            else {
                return "";
            }
        }
        else {
            return "La cedula excede de 10 digitos <br>"
        }
    }
    return '';
}

function validarCedula(cad) {
    var patron = /\d{5,10}/;
    if (cad.length < 5) {
        return "La cedula es de al menos 5 digitos";
    }
    else {
        if (cad.length <= 10) {
            if (!patron.test(cad)) {
                return 'La cedula solo debe incluir digitos <br>'
            }
            else {
                return "";
            }
        }
        else {
            return "La cedula excede de 10 digitos <br>"
        }
    }
    return '';
}



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
    formData["sel3"] = document.getElementById("sel3").value;
    formData["especialidad"] = document.getElementById("especialidad").value;
    formData["cedula"] = document.getElementById("cedula").value;
    formData["idDocente"] = document.getElementById("idDocente").value;
    formData["idCarrera"] = document.getElementById("idCarrera").value;
    formData["idUsuario"] = document.getElementById("idUsuario").value;
    return formData;
}

function añadirElemento(data) {
    var table = document.getElementById("altaDocentes").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.noControl;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.sel3;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.especialidad;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.cedula;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.idDocente;
    cell6 = newRow.insertCell(5);
    cell6.innerHTML = data.idCarrera;
    cell7 = newRow.insertCell(6);
    cell7.innerHTML = data.idUsuario;
    cell7 = newRow.insertCell(7);
    cell7.innerHTML = `<a onClick="editarElementos(this)">Editar</a>
                       <a onClick="Eliminar(this)">Eliminar</a>`;
}

function limpearElementos() {
    document.getElementById("noControl").value = "";
    document.getElementById("sel3").value = "------------Seleccionar------------";
    document.getElementById("especialidad").value = "";
    document.getElementById("cedula").value = "";
    document.getElementById("idDocente").value = "";
    document.getElementById("idCarrera").value = "";
    document.getElementById("idUsuario").value = "";
    selectedRow = null;
}

function editarElementos(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("noControl").value = selectedRow.cells[0].innerHTML;
    document.getElementById("sel3").value = selectedRow.cells[1].innerHTML;
    document.getElementById("especialidad").value = selectedRow.cells[2].innerHTML;
    document.getElementById("cedula").value = selectedRow.cells[3].innerHTML;
    document.getElementById("idDocente").value = selectedRow.cells[4].innerHTML;
    document.getElementById("idCarrera").value = selectedRow.cells[5].innerHTML;
    document.getElementById("idUsuario").value = selectedRow.cells[6].innerHTML;
}

function actualizarElementos(formData) {
    selectedRow.cells[0].innerHTML = formData.noControl;
    selectedRow.cells[1].innerHTML = formData.sel3;
    selectedRow.cells[2].innerHTML = formData.especialidad;
    selectedRow.cells[3].innerHTML = formData.cedula;
    selectedRow.cells[4].innerHTML = formData.idDocente;
    selectedRow.cells[5].innerHTML = formData.idCarrera;
    selectedRow.cells[6].innerHTML = formData.idUsuario;
}

function Eliminar(td) {
    if (confirm('Deseas eliminar al Docente?')) {
        row = td.parentElement.parentElement;
        document.getElementById("altaDocentes").deleteRow(row.rowIndex);
        actualizarElementos();
    }
}

function validacion(form) {
    var noCl = form.noControl.value;
    var mensaje = validarNoControl(noCl);

    if (mensaje != '') {
        var div = document.getElementById("notificaciones");
        div.innerHTML = '<p>' + mensaje + '</p>';;
        div.style.color = "red";
        return false;
    } else {
        return true;
    }

}

function validar() { //SCRIPT ANTI (GESTION,CONTA,INDUSTRIAL,ETC) 
    //isValid = true;
    if (document.getElementById("noControl").value == "") {
        isValid = false;
        alert('Error: (No.Control) vacio, porfavor intentalo de nuevo :/');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    if (document.getElementById("especialidad").value == "") {
        isValid = false;
        alert('Error: (Especialidad) vacia, porfavor intentalo de nuevo :/');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }


    if (document.getElementById("cedula").value == "") {
        isValid = false;
        //console.alert("CEDULA CORRECTA")
        alert('Error: Formato de cedula incorrectos :(');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    

    if (document.getElementById("idDocente").value == "") {
        isValid = false;
        //console.alert("CEDULA CORRECTA")
        alert('Error: (idDocente) vacio, intentalo de nuevo :(');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    if (document.getElementById("idCarrera").value == "") {
        isValid = false;
        //console.alert("CEDULA CORRECTA")
        alert('Error: (idCarrera) vacio, intentalo de nuevo :(');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    if (document.getElementById("idUsuario").value == "") {
        isValid = false;
        //console.alert("CEDULA CORRECTA")
        alert('Error: (idUsuario) vacio, intentalo de nuevo :(');
        document.getElementById("fullNameValidationError").classList.remove("hide");
    }

    else {
        isValid = true;
        if (!document.getElementById("fullNameValidationError").classList.contains("hide"))
            document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;
}