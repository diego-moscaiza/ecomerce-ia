import type { APIRoute } from "astro";
import axios from "axios";

export const POST: APIRoute = async ({ request, redirect }) => {
    try {
        const data = await request.formData();
        const nombre = data.get("nombre")?.toString();
        const apellido = data.get("apellido")?.toString();
        const documento = data.get("documento")?.toString();
        const fecha_nacimiento = data.get("fecha_nacimiento")?.toString();
        const sexo = data.get("sexo")?.toString();
        const telefono = data.get("telefono")?.toString();
        const correo = data.get("correo")?.toString();
        const contraseña = data.get("contraseña")?.toString();
        const apiUrl = "https://ecomerce-ia.onrender.com/api/clientes/register/";
        const response = await axios.post(apiUrl, {
            nombre,
            apellido,
            documento,
            fecha_nacimiento,
            sexo,
            telefono,
            correo,
            contraseña,
        });
        if (response.status === 201) {
            // Mostrar una respuesta de registro de cuenta exitosa
            console.log(`Se ha registrado el correo ${correo} exitosamente`);
            // Redirigir a otra página
            return redirect("/iniciar-sesion");
        } else {
            console.error("Estado del servidor:", response.statusText);
            console.log(response);
        }
    } catch (error) {
        if (error instanceof Error) {
            console.error("Error al crea cuenta:", error.message);
        }
    }
}
