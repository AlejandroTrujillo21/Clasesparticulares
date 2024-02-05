<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST["name"];
    $email = $_POST["email"];
    $edad = $_POST["date"];
    $mensaje = $_POST["subject"];

   
    $destinatario = "atcriado@gmail.com";
    $asunto = "Solicitud de clase de $nombre";
    $contenido = "Nombre: $nombre\nEmail: $email\nEdad: $edad\nMensaje: $mensaje";
    mail($destinatario, $asunto, $contenido);

    // Redirigir o mostrar un mensaje de éxito.
    header("Location: index.html");
} else {
    // Si alguien intenta acceder directamente a este script, puedes redirigirlos a la página principal u otra página.
    header("Location: index.html");
}
?>
