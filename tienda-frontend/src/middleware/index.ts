import { defineMiddleware } from "astro:middleware";
import micromatch from "micromatch";

const publicRoutes = ["/", "/prendas", "/iniciar-sesion", "/registrarse"];
const protectedRoutes = ["/cesta", "/compras"];
const redirectRoutes = ["/iniciar-sesion", "/registrarse"];

export const onRequest = defineMiddleware(
    async ({ locals, url, cookies, redirect }, next) => {
        if (micromatch.isMatch(url.pathname, publicRoutes)) {
            cookies.get("access-token");
            cookies.get("userData");

            // Retrieve user data from cookie
            const userData = cookies.get("userData");
            if (userData) {
                // Store user data in locals
                locals.first_name = userData.json().first_name;
                locals.last_name = userData.json().last_name;
                locals.username = userData.json().username;
                locals.email = userData.json().email;
                locals.is_logged = true
            }

            // If the route is public, allow the request to continue
            return next();
        }

        if (micromatch.isMatch(url.pathname, protectedRoutes)) {
            const accessToken = cookies.get("access-token");
            const userData = cookies.get("userData");

            if (accessToken && userData) {
                // Retrieve user data from cookie
                const userDataJson = userData.json();
                locals.first_name = userDataJson.first_name;
                locals.last_name = userDataJson.last_name;
                locals.username = userDataJson.username;
                locals.email = userDataJson.email;
                locals.is_logged = true;
            } else {
                return redirect("/iniciar-sesion");
            }
        }

        if (micromatch.isMatch(url.pathname, redirectRoutes)) {
            const accessToken = cookies.get("access-token");
            const userData = cookies.get("userData");

            if (accessToken && userData) {
                return redirect("/");
            }
        }

        return next();
    });
