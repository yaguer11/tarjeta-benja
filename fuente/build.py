# Genera ../index.html a partir de template.html.
# Las imagenes se copian a ../img/ y se enlazan como archivos (asi el HTML queda liviano
# y WhatsApp puede leer la vista previa del link).
import re, shutil, os
t = open('template.html', encoding='utf-8').read()
os.makedirs('../img', exist_ok=True)
def rep(m):
    name = m.group(1)
    shutil.copyfile(f'src/{name}.webp', f'../img/{name}.webp')
    return f'img/{name}.webp'
open('../index.html', 'w', encoding='utf-8').write(re.sub(r'\{\{(\w+)\}\}', rep, t))
