let loggedIn = sessionStorage.getItem("logged_in");

function updateButtons() {
  if (loggedIn) {
    // Si el usuario ha iniciado sesión, mostrar el botón de "Cerrar sesión" y ocultar el de "Iniciar sesión"
    document.getElementById("login-btn").style.display = "none";
    document.getElementById("logout-btn").style.display = "block";
  } else {
    // Si el usuario no ha iniciado sesión, mostrar el botón de "Iniciar sesión" y ocultar el de "Cerrar sesión"
    document.getElementById("login-btn").style.display = "block";
    document.getElementById("logout-btn").style.display = "none";
  }
}

window.onload = function () {
  updateButtons();
};

function login() {
  // Aquí deberías tener el código para iniciar sesión
  // Después de iniciar sesión, establece la variable de sesión
  sessionStorage.setItem("logged_in", true);
  // Actualiza los botones
  updateButtons();
}

function logout() {
  // Aquí deberías tener el código para cerrar sesión
  // Después de cerrar sesión, elimina la variable de sesión
  sessionStorage.removeItem("logged_in");
  // Actualiza los botones
  updateButtons();
}

document.getElementById("login-btn").addEventListener("click", login);
document.getElementById("logout-btn").addEventListener("click", logout);
