import base64,re
t=open('template.html',encoding='utf-8').read()
def rep(m):
    return 'data:image/webp;base64,'+base64.b64encode(open(f'src/{m.group(1)}.webp','rb').read()).decode()
open('../index.html','w',encoding='utf-8').write(re.sub(r'\{\{(\w+)\}\}',rep,t))
