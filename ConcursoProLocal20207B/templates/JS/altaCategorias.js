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
        formData["nCategoria"] = document.getElementById("nCategoria").value;
        formData["sel2"] = document.getElementById("sel2").value;
        formData["idCategoria"] = document.getElementById("idCategoria").value;
        formData["idProblemasPropuesto"] = document.getElementById("idProblemasPropuesto").value;
        return formData;
    }

    function añadirElemento(data) {
        var table = document.getElementById("altaCategoria").getElementsByTagName('tbody')[0];
        var newRow = table.insertRow(table.length);
        cell1 = newRow.insertCell(0);
        cell1.innerHTML = data.nCategoria;
        cell2 = newRow.insertCell(1);
        cell2.innerHTML = data.sel2;
        cell3 = newRow.insertCell(2);
        cell3.innerHTML = data.idCategoria;
        cell4 = newRow.insertCell(3);
        cell4.innerHTML = data.idProblemasPropuesto;
        cell4 = newRow.insertCell(4);
        cell4.innerHTML = `<a onClick="editarElementos(this)">Editar</a>
                       <a onClick="Eliminar(this)">Eliminar</a>`;
    }

    function limpearElementos() {
        document.getElementById("nCategoria").value = "";
        document.getElementById("sel2").value = "------------Seleccionar------------";
        document.getElementById("idCategoria").value = "";
        document.getElementById("idProblemasPropuesto").value = "";
        selectedRow = null;
    }

    function editarElementos(td) {
        selectedRow = td.parentElement.parentElement;
        document.getElementById("nCategoria").value = selectedRow.cells[0].innerHTML;
        document.getElementById("sel2").value = selectedRow.cells[1].innerHTML;
        document.getElementById("idCategoria").value = selectedRow.cells[2].innerHTML;
        document.getElementById("idProblemasPropuesto").value = selectedRow.cells[3].innerHTML;
    }

    function actualizarElementos(formData) {
        selectedRow.cells[0].innerHTML = formData.nCategoria;
        selectedRow.cells[1].innerHTML = formData.sel2;
        selectedRow.cells[2].innerHTML = formData.idCategoria;
        selectedRow.cells[3].innerHTML = formData.idProblemasPropuesto;
    }

    function Eliminar(td) {
        if (confirm('Deseas eliminar esta categoria?')) {
            row = td.parentElement.parentElement;
            document.getElementById("altaCategoria").deleteRow(row.rowIndex);
            actualizarElementos();
        }
    }

    function validar() { //SCRIPT ANTI (GESTION,CONTA,INDUSTRIAL,ETC) 
        isValid = true;
        if (document.getElementById("nCategoria").value == "") {
            isValid = false;
            alert('Error: (Categoria) vacia, por favor intentalo de nuevo :)');
            document.getElementById("fullNameValidationError").classList.remove("hide");
        }

        if (document.getElementById("idCategoria").value == "") {
            isValid = false;
            alert('Error: (idCategoria) vacio, por favor intentalo de nuevo :)');
            document.getElementById("fullNameValidationError").classList.remove("hide");
        }

        if (document.getElementById("idProblemasPropuesto").value == "") {
            isValid = false;
            alert('Error: (idProblemasPropuesto) vacio, por favor intentalo de nuevo :)');
            document.getElementById("fullNameValidationError").classList.remove("hide");
        }

        else {
            isValid = true;
            if (!document.getElementById("fullNameValidationError").classList.contains("hide"))
                document.getElementById("fullNameValidationError").classList.add("hide");
        }
        return isValid;

    }
   