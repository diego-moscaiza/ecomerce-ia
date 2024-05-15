import axios from "axios";

export const loginUser = () => {
  return axios.post("http://127.0.0.1:8000/login")
}


// document.getElementById('loginForm').addEventListener('submit', async (event) => {
//   event.preventDefault();

//   const formData = new FormData(event.target);

//   try {
//     const response = await fetch('/api/login/', {
//       method: 'POST',
//       body: formData,
//     });

//     if (!response.ok) {
//       throw new Error('Network response was not ok');
//     }

//     const data = await response.json();
//     console.log(data);
//     // Handle successful login
//   } catch (error) {
//     console.error(error);
//     // Handle error
//   }
// });
