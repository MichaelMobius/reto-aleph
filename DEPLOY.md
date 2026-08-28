# Despliegue robusto

## Recomendado

Sirve esta carpeta como sitio estático en el proveedor que prefieras. La prueba de Git está encapsulada en `artifacts/memory-case.bundle`; **no requiere conservar el `.git` de este proyecto**.

Antes de publicar:

```bash
python tools/verify_release.py
```

Después de publicar:

```bash
python tools/verify_http.py https://tu-dominio.example/
```

## GitHub Pages

GitHub Pages funciona, pero si el repositorio es público la URL estándar puede revelar el nombre del repo y facilita descargar el árbol completo. Para una experiencia más auténtica:

1. usa un dominio personalizado, o
2. publica el build en un hosting estático distinto del repositorio de autoría, o
3. acepta que, al ser un CTF 100% client-side, un estudiante decidido siempre puede descargar los recursos públicos y analizarlos en lote.

Un dominio personalizado oculta la pista obvia de la URL, pero no convierte en secreto un repositorio público. Si necesitas gates técnicamente secretos, hace falta un componente servidor.

## Three.js

La visualización 3D carga Three.js desde CDN. El CTF sigue siendo resoluble si falla WebGL; usa `?lite=1` para forzar el modo liviano.

## Capas posteriores

`codex/` y `comedia/` son artefactos estáticos. El flujo normal los desbloquea mediante estado local después de resolver las capas anteriores. Como todo el laboratorio es client-side, inspeccionar el árbol puede revelar su existencia; esto se considera análisis del artefacto, no una frontera de seguridad.

## Paquete GitHub Pages

Esta edición incluye `.nojekyll` y usa rutas compatibles con Project Sites (`https://usuario.github.io/repositorio/`). Consulta `GITHUB_PAGES.md`.
