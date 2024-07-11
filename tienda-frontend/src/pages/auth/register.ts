import type { APIRoute } from 'astro';

const apiUrl = "https://ecomerce-ia.onrender.com/api/cuentas/register/";

export const POST: APIRoute = async ({ request, redirect }) => {
    try {
        const formData = await request.formData();
        const nombre = formData.get("first_name")?.toString();
        const apellido = formData.get("last_name")?.toString();
        const correo = formData.get("email")?.toString();;
        const usuario = formData.get("username")?.toString();;
        const password = formData.get("password")?.toString();;

        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                first_name: nombre,
                last_name: apellido,
                email: correo,
                username: usuario,
                password: password,
            }),
        });

        if (!usuario || !password) {
            return new Response("Usuario y contraseña son requeridos.", { status: 400 });
        }

        if (response.ok) {
            console.log(`Se ha registrado exitosamente.`);
            // Redirigir a otra página
            return redirect("/iniciar-sesion");
        } else {
            return new Response("Error al crea cuenta:", { status: 401 });
        }
    }
    catch (error) {
        if (error instanceof Error) {
            console.error("Error al crea cuenta:", error.message);
            return new Response("Error al crea cuenta:", { status: 500 });
        }
    }
}
