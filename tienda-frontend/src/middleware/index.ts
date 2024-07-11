import { defineMiddleware } from "astro:middleware";
import micromatch from "micromatch";

const publicRoutes = ["/", "/prendas", "/iniciar-sesion", "/registrarse"];
const protectedRoutes = ["/prendas/*", "/cesta", "/compras"];
const redirectRoutes = ["/iniciar-sesion", "/registrarse"];

export const onRequest = defineMiddleware(
    async ({ locals, url, cookies, redirect }, next) => {
        if (micromatch.isMatch(url.pathname, publicRoutes)) {
            cookies.get("access-token");
            cookies.get("userData");

            // If the route is public, allow the request to continue
            return next();
        }

        if (micromatch.isMatch(url.pathname, protectedRoutes)) {
            const accessToken = cookies.get("access-token");
            const userData = cookies.get("userData");

            if (!accessToken) {
                return redirect("/iniciar-sesion");
            }

            let userDataValue;
            if (userData) {
                try {
                    userDataValue = JSON.parse(userData.value);
                } catch (error) {
                    console.error("Error al parsear userData:", error.message);
                    userDataValue = "";
                }
            }

            console.log(accessToken.value);
            console.log(userDataValue);

            // Set the cookie with the API token
            // cookies.set("access-token", accessToken, {
            //     path: "/",
            //     secure: true,
            //     sameSite: "strict",
            // });

            // // Set the cookie with the user data
            // cookies.set("userData", userData, {
            //     path: "/",
            //     secure: true,
            //     sameSite: "strict",
            // });
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
