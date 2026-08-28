# Publicar RETO ALEPH 100 en GitHub Pages

Este paquete está preparado para un **Project Site** de GitHub Pages, por ejemplo:

`https://USUARIO.github.io/REPOSITORIO/`

## Opción simple: Deploy from a branch

1. Crea un repositorio nuevo en GitHub.
2. Sube **el contenido de esta carpeta a la raíz del repositorio**. `index.html` debe quedar en la raíz.
3. Conserva el archivo vacío `.nojekyll`.
4. Ve a **Settings → Pages**.
5. En **Build and deployment**, selecciona **Deploy from a branch**.
6. Elige la rama `main` y la carpeta `/(root)`.
7. Guarda y abre la URL que GitHub muestre en **Visit site**.

## Verificación local antes de subir

```bash
python tools/verify_release.py
```

## Verificación después de publicar

```bash
python tools/verify_http.py https://USUARIO.github.io/REPOSITORIO/
```

## Importante para este CTF

- `.nojekyll` es intencional: el sitio contiene `/.well-known/security.txt` y debe publicarse como estático sin transformación de Jekyll.
- Las rutas internas son relativas y funcionan bajo `/REPOSITORIO/`.
- `?lite=1` funciona sin cargar Three.js remoto.
- El modo 3D normal intenta cargar Three.js desde jsDelivr y cae a Canvas2D si no está disponible.
- Al ser un CTF 100% client-side, un repositorio público permite descargar y auditar todo el árbol. Esto es parte del modelo de amenaza del proyecto, no una frontera de seguridad.
