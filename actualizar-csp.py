"""Recalcula los hashes de la Content-Security-Policy del portafolio.

La CSP solo permite ejecutar los <script> en línea cuyo hash SHA-256 coincide.
Si editas cualquier script de la página, ejecuta:

    python actualizar-csp.py

y el meta de la CSP se actualiza con los hashes nuevos.
"""
import base64
import hashlib
import re
import sys
from pathlib import Path

PAGE = Path(__file__).with_name("index.html")

html = PAGE.read_text(encoding="utf-8")
scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
hashes = " ".join(
    "'sha256-%s'" % base64.b64encode(hashlib.sha256(s.encode("utf-8")).digest()).decode()
    for s in scripts
)
new_html, n = re.subn(r"script-src [^;]+;", "script-src %s;" % hashes, html, count=1)
if n != 1:
    sys.exit("No encontré la directiva script-src en el meta de la CSP.")
PAGE.write_text(new_html, encoding="utf-8")
print("CSP actualizada con %d scripts." % len(scripts))
