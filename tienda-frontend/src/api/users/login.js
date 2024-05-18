import axios from "axios";

const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const apiUrl = 'http://127.0.0.1:8000/api/users/create/';
  const formData = new FormData(loginForm);
  try {
    const response = await axios.post(apiUrl, formData);
    const { user } = response.data;
    // Handle successful login response
    console.log(`Logged in successfully! User: ${user}`);
  } catch (error) {
    console.error('Error logging in:', error);
  }
});
