function regresar(url){
    location.href='/'+url;
}
function verPassword(){
    if(document.getElementById("check").checked)
        document.getElementById("password").setAttribute("type","text")
   else
        document.getElementById("password").setAttribute("type","password")
}