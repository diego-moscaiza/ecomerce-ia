import type { APIRoute } from "astro";
import axios from "axios";

export const POST: APIRoute = async ({ request, redirect }) => {
    try {
        const formData = await request.formData();
        const correo = formData.get("correo")?.toString();
        const contraseña = formData.get("contraseña")?.toString();
        //const apiUrl = "https://ecomerce-ia.onrender.com/api/clientes/login/";
        const apiUrl = "http://127.0.0.1:8000/api/clientes/login/";
        const response = await axios.post(apiUrl, { correo, contraseña });

        if (response.status === 200) {
            // Manejar una respuesta de inicio de sesión exitosa
            console.log(`Haz iniciado sesión! Usuario: ${correo}`);
            // Redirigir al usuario a la página de inicio
            return redirect("/");
        } else {
            throw new Error("Error al iniciar sesión");
        }
    } catch (error) {
        if (error instanceof Error) {
            console.error("Error al iniciar sesión:", error.message);
        }
    }
}
