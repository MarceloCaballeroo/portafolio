# Portafolio · Marcelo Caballero Olave

Portafolio personal en un solo `index.html` (sin build, sin dependencias): modo **cockpit** inmersivo y modo **profesional** (CV), en español e inglés.

## Estructura
- `index.html`: todo el sitio (HTML, CSS y JS).
- `fonts/`, `img/`: fuentes autoalojadas (licencias OFL incluidas) e imágenes.
- `Marcelo-Caballero-CV.pdf`: CV descargable.
- `vercel.json`: cabeceras de seguridad (CSP, HSTS, etc.).
- `actualizar-csp.py`: **ejecutar después de editar cualquier `<script>`** para recalcular los hashes de la CSP.

## Probar en local
```bash
python -m http.server 8765 --bind 127.0.0.1
```
Abrir http://127.0.0.1:8765

## Despliegue
Sitio estático: se publica en Vercel, Cloudflare Pages o GitHub Pages sin configuración de build.
