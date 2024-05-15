# Kit de inicio de Astro

## 🚀 Estructura del proyecto

Dentro de su proyecto Astro, verá las siguientes carpetas y archivos:

```text
/
├── public/
├── src/
│   └── pages/
│       └── index.astro
└── package.json
```

Astro busca archivos `.astro` o `.md` en el directorio `src/pages/`. Cada página se expone como una ruta según su nombre de archivo.

No hay nada especial en `src/components/`, pero ahí es donde nos gusta colocar los componentes Astro/React/Vue/Svelte/Preact.

Cualquier activo estático, como imágenes, se puede colocar en el directorio `public/`.

## 🧞 Comandos

Primero debe de instalar pnpm, que es una alternativa a npm.

`corepack enable pnpm`

Ahora estos los comandos se ejecutan desde la raíz del proyecto, desde una terminal:

| Dominio                   | Acción                                                                         |
| :------------------------ | :----------------------------------------------------------------------------- |
| `pnpm install`             | Instala dependencias                                                           |
| `pnpm run dev`             | Inicia el servidor de desarrollo local en `localhost:4321`                     |
| `pnpm run build`           | Construya su sitio de producción para `./dist/`                                |
| `pnpm run preview`         | Obtenga una vista previa de su compilación localmente, antes de implementarla. |
| `pnpm run astro ...`       | Ejecute comandos CLI como `astro add`, `astro check`                           |
| `pnpm run astro -- --help` | Obtenga ayuda para usar Astro CLI                                              |

## 👀 ¿Querer aprender más?

No dudes en consultar [nuestra documentación](https://docs.astro.build) o acceder a nuestro [servidor de Discord](https://astro.build/chat).
