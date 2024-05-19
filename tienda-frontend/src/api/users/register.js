import axios from "axios";

const loginForm = document.getElementById('register-form');


loginForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const apiUrl = 'http://127.0.0.1:8000/api/clientes/register/';
  const correo = document.getElementById('correo').value;
  const contraseña = document.getElementById('contraseña').value;
  const data = { correo, contraseña };
  try {
    await axios.post(apiUrl, data);
    // Handle successful login response
    console.log(`Haz iniciado sesión! Usuario: ${data.correo}`);
  } catch (error) {
    console.error('Error al iniciar sesión:', error);
  }
});
