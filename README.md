# RETO ALEPH — LABERINTO

CTF educativo estático y no lineal que fusiona y amplía RETO ALEPH 2 + 3.

## Estructura conocida al inicio

- 42 estaciones visibles distribuidas en 7 anillos.
- Cada anillo tiene 3 puertas independientes; cada puerta contiene una pareja de retos.
- Los anillos se pueden resolver en cualquier orden.
- El metarreto Ω requiere reconstruir las siete palabras de seis letras.
- Existen rutas matemáticas subterráneas que atraviesan estaciones no consecutivas.
- El primer subsuelo completa 53 nodos.
- Tras el campo primo 53 aparece CODEX, un segundo subsuelo dedicado a formas de codificación que llega hasta el espejo 91.
- El sistema puede contener capas posteriores que no se documentan aquí.

## Áreas

1. FUENTE — HTML, JavaScript, DOM, query strings, cookies, localStorage
2. CODIFICACIÓN — Base64, URL encoding, hexadecimal, binario, Morse, ROT13
3. CIFRAS — César, Atbash, Vigenère, Rail Fence, Polybius, Bacon
4. RASTROS — XOR, SHA-256, JWT ficticio, Network, Source Maps, CSS/SVG
5. BIBLIOTECA — Borges, El Aleph, Biblioteca Nacional, Project Gutenberg
6. CARTOGRAFÍA — historia de Internet, Google Maps/GPS, Bletchley Park, Apollo 11
7. MEMORIA — robots.txt, Git forensics, Web Manifest, Service Worker, PNG, .well-known

## Seguridad

Todo ocurre en un laboratorio deliberadamente vulnerable y en fuentes públicas. No escanees, ataques ni pruebes credenciales contra servicios externos.

## Ejecutar localmente

```bash
python -m http.server 8000
```

## Despliegue

La estación de Git no depende del historial del repositorio de producción: usa `artifacts/memory-case.bundle`. El sitio puede desplegarse desde un repositorio nuevo, por upload estático o desde otro proveedor sin romper la prueba. Lee `DEPLOY.md`.

## Interfaz JODI / Three.js

Esta edición usa una estética de net.art inspirada en la lógica material de JODI: código, errores, rutas, tipografía monoespaciada y comportamiento del navegador aparecen como parte de la interfaz. No reproduce páginas ni ASCII del colectivo.

- `assets/aleph3d.js`: escena WebGL procedural y reactiva.
- `?lite=1`: desactiva WebGL conservando toda la funcionalidad.
- `prefers-reduced-motion`: reduce el movimiento automáticamente.

Para uso completamente offline, sirve Three.js localmente y cambia el import correspondiente.

## CODEX

CODEX agrupa códigos de máquina, telegrafía/señal humana, cifras algebraicas, integridad/corrección de errores, compresión, códigos visuales y protocolos/señales. No es lineal.


## Robustez de la versión candidata

- Los retos de investigación y GPS posteriores ya no guardan su respuesta en texto plano.
- CODEX y COMEDIA usan pruebas derivadas de la solución para validar el estado local; editar un valor simple en `localStorage` ya no completa un gate.
- `?lite=1` no intenta cargar Three.js. Si el CDN no está disponible, aparece una capa visual local de degradación en canvas en vez de una página rota.
- `python tools/verify_release.py` incluye comprobaciones contra regresiones funcionales detectadas durante la auditoría adversarial.
