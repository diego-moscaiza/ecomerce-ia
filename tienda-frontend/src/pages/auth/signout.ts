import type { APIRoute } from 'astro';

export const GET: APIRoute = async ({ cookies, locals, redirect }) => {
  try {
    // const accessToken = cookies.get('access-token')?.value;

    // if (!accessToken) {
    //   return new Response("No se proporcionó un token de refresh", { status: 401 });
    // }

    // const response = await fetch('https://ecomerce-ia.onrender.com/api/cuentas/logout/', {
    //   method: 'POST',
    //   headers: {
    //     'Authorization': `Bearer ${accessToken}`,
    //   },
    // });

    // if (response.ok) {
    //   // Eliminar las cookies de token y userData
      cookies.delete('access-token', { path: "/" });
      cookies.delete('userData', { path: "/" });
      locals.is_logged = false;
      console.log("Sesión cerrada")
      console.log(`is_logged: ${locals.is_logged}`)
      // Redirigir a la página de inicio
      return redirect("/iniciar-sesion");
    // } else if (response.status === 401) {
    //   return new Response("Token no válido", { status: 401 });
    // }
  } catch (error) {
    console.error("Error al cerrar sesión:", error.message);
    return new Response("Error al cerrar sesión", { status: 500 });
  }
};
