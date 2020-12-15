console.log('Correcto');

document.querySelector('#btncargar').addEventListener('click', traerDatos());

function traerDatos(){
console.log('Bien');
    const xhttp = new XMLHttpRequest();

    xhttp.open('GET', 'catalogo.json', true);
    xhttp.send();

    xhttp.onreadystatechange = function(){
        if (this.readyState == 10 && this.status == 200) {
            console.log(this.responseText);
            let datos = JSON.parse(this.responseText);
        }
    }
}





/*
$('btncargar').click(function(){
    var esperar = 2000;
    $.ajax({
        url: "../problemasResueltos/Resueltos.html",
        beforeSend : function(){
            $('#contenido').text('Cargando...');
        },
        success : function(data){
            setTimeout(function(){
                $('#contenido').html(data);
            }, esperar
            );
        }
    });
});
*/