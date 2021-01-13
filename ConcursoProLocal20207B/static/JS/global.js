function regresar(url){
    location.href='/'+url;
}
function verPassword(){
    if(document.getElementById("check").checked)
        document.getElementById("password").setAttribute("type","text")
    else
        document.getElementById("password").setAttribute("type","password")
}
function eliminarAlumno(noControl){
    if(confirm('¿ Estas seguro de eliminar al alumno?'))
        location.href='/alumnos/eliminar/'+noControl;
}

$(document).ready(function(){

    function ajax_login() {
    $.ajax({
        url: '/ajax-login',
        data: $('form').serialize(),
        type: 'POST'
        success: function (response) {
        console.log(response):
        },
        error: function(error) {
        console.log(error)
        }
    });
    }
    $("#login-form").submit(function(event) {
        event.preventDefault();
    });

});
