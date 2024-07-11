import type { APIRoute } from 'astro';

export const GET: APIRoute = async ({ cookies, redirect }) => {
  try {
    const accessToken = cookies.get('access-token')?.value;

    if (!accessToken) {
      return new Response("No se proporcionó un token de refresh", { status: 401 });
    }

    const response = await fetch('https://ecomerce-ia.onrender.com/api/cuentas/logout/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });

    if (response.ok) {
      // Eliminar las cookies de token y userData
      cookies.delete('access-token', { path: "/" });
      cookies.delete('refresh-token', { path: "/" });
      cookies.delete('userData', { path: "/" });

      // Redirigir a la página de inicio
      return redirect("/");
    } else if (response.status === 401) {
      return new Response("Token no válido", { status: 401 });
    }
  } catch (error) {
    console.error("Error al cerrar sesión:", error.message);
    return new Response("Error al cerrar sesión", { status: 500 });
  }
};
