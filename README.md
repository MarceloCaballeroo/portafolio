# Portafolio · Marcelo Caballero Olave

Portafolio personal en un solo `index.html` (sin build, sin dependencias): modo **cockpit** inmersivo y modo **profesional** (CV), en español e inglés.

## Estructura
- `index.html`: todo el sitio (HTML, CSS y JS).
- `fonts/`, `img/`: fuentes autoalojadas (licencias OFL incluidas) e imágenes.
- `Marcelo-Caballero-CV.pdf` y `Marcelo-Caballero-CV-EN.pdf`: CV descargable en español e inglés (2 páginas, texto seleccionable para ATS).
- `_headers` (Cloudflare Pages) y `vercel.json` (Vercel): cabeceras de seguridad (CSP, HSTS, etc.).
- `actualizar-csp.py`: **ejecutar después de editar cualquier `<script>`** para recalcular los hashes de la CSP.

## Probar en local
```bash
python -m http.server 8765 --bind 127.0.0.1
```
Abrir http://127.0.0.1:8765

## Despliegue
Sitio estático en Cloudflare Pages (sin comando de build, directorio de salida `/`).
