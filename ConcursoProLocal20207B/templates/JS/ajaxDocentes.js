function ajax() {
    const http = new XMLHttpRequest();
    const url = 'http://localhost/templates/ajaxkalis.html';

    http.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) { //SI SE CUMPLEN AMBAS CONDICIONES LA SOLICITUD ES EXITOSA
            console.log(this.responseText);
            document.getElementById("notificaciones").innerHTML = this.responseText;
        }
    }
    http.open("GET",url);
    http.send(); 
}
document.getElementById('ajaxButton').addEventListener("click",function(){
    ajax();
})