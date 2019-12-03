function enviarMensaje(){
    alert("Mensaje Enviado");
}
function mensajeCompra(){
    alert("Aun no hemos agregado redcompra, esta es una version de prueba");
}
$(document).ready(function(){
    $('.flecharriba').click(function(){
        $('body, html').animate({
            scrollTop: '0px'
        });
    });

    $(window).scroll(function(){
        if($(this).scrollTop() > 0){
            $('.flecharriba').slideDown(600);
        } else{
            $('.flecharriba').slideUp(600);
        };
    });

});

// --------------------------VALIDACION DE PANTALLA CONTACTO


function validarNombre() {

    var nombre = document.getElementById("nombre").value;
    var txtNombre = document.getElementById("nombre");

    //Test campo obligatorio
    if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
        alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
        txtNombre.classList.add('error');
    } else {
        txtNombre.classList.remove('error');
    }
}

function validarCorreo() {

    var correo = document.getElementById("mail").value;
    var txtCorreo = document.getElementById("mail");

    //Test correo
    if (correo == null || correo.length == 0 || !(/\S+@\S+\.\S+/.test(correo))) {
        alert('ERROR: Debe escribir un correo válido');
        txtCorreo.classList.add('error');
    } else {
        txtCorreo.classList.remove('error');
    }
}

$(function() {
    $('#nombre').on('blur', function() {
        var nombre = $('#nombre').val();

        if (nombre == null || nombre.length == 0) {
            alert('ERROR: El campo nombre no debe ir vacío' + nombre);
            $('#nombre').addClass('error');
            $('#nombre').removeClass('exito');
        } else {
            $('#nombre').removeClass('error');
            $('#nombre').addClass('exito');
        }


    })
});

$(function() {
    $('#mail').on('blur', function() {
        var mail = $('#mail').val();

        if (mail == null || mail.length == 0) {
            alert('ERROR: El campo email no debe ir vacío');
            $('#mail').addClass('error');
            $('#mail').removeClass('exito');
        } else {
            $('#mail').removeClass('error');
            $('#mail').addClass('exito');
        }

    })
});

function validarFormulario() {
    validarNombre();
    validarCorreo()
}