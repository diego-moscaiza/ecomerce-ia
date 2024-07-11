import type { APIRoute } from 'astro';

const apiUrl = "https://ecomerce-ia.onrender.com/api/cuentas/login-user/";

export const POST: APIRoute = async ({ request, cookies, redirect }) => {
    try {
        const formData = await request.formData();
        const usuario = formData.get("username")?.toString();
        const password = formData.get("password")?.toString();

        if (!usuario || !password) {
            return new Response("Usuario y contraseña son requeridos.", { status: 400 });
        }

        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: usuario,
                password: password
            })
        });

        if (response.ok) {
            const responseData = await response.json();

            // // Set cookies
            cookies.set('access-token', responseData.token, {
                path: "/",
                secure: true,
                sameSite: 'strict'
            });

            cookies.set('userData', responseData.user, {
                path: "/",
                secure: true,
                sameSite: 'strict'
            });

            console.log(responseData.token);
            console.log(responseData.user);

            // Redirect to home page
            return redirect("/");
        } else {
            return new Response("Error al iniciar sesión", { status: 401 });
        }
    } catch (error) {
        if (error instanceof Error) {
            console.error("Error al iniciar sesión:", error.message);
            return new Response("Error al iniciar sesión", { status: 500 });
        }
    }
};
