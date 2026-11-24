# Genera proyectos/<id>.html a partir de PROYECTOS.
# Uso: python3 herramientas/generar_proyectos.py  (desde la carpeta del sitio)
import html, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent

PROYECTOS = [
  dict(id='ambar', name='Ambar', sub='Ecommerce por encargo', url='https://ambarsv.com', label='ambarsv.com',
       color='#E2A04A', ink='#5A3A10', tags=['Ecommerce', 'Marca', 'Panel de ventas'],
       intro='Tienda en línea para traer productos por encargo desde EE. UU. a El Salvador. Los clientes compran desde el celular y el dueño maneja todo el negocio desde un solo panel.',
       screens=[('ambar-1', 'Inicio con cuenta regresiva del cierre de pedidos'), ('ambar-2', 'Ficha de producto con notas y precio'), ('ambar-3', 'Carrito con productos, total y fecha de entrega')],
       admin=[
         ('Ver sus ventas al día', 'Vendido, cobrado, por cobrar, ticket promedio y unidades vendidas por periodo.'),
         ('Entender qué funciona', 'Gráficas de ventas por semana y por categoría, y los productos más pedidos.'),
         ('Manejar pedidos', 'Revisar cada pedido por estado (pendiente, confirmado, entregado o cancelado) y editarlo.'),
         ('Administrar el catálogo', 'Crear y editar productos, ponerlos en oferta, marcar si hay stock o es por encargo, y mostrarlos u ocultarlos.'),
         ('Programar el cierre de pedidos', 'Los clientes ven una cuenta regresiva hasta la fecha límite.'),
         ('Escuchar a los clientes', 'Recibir las sugerencias de productos que piden.'),
       ]),
  dict(id='hogareno', name='Hogareño', sub='Servicios para el hogar', url='https://www.xn--hogareo-9za.app', label='hogareño.app',
       color='#4642A0', ink='#1C1A3D', tags=['App', 'Supabase', 'Marca'],
       intro='Plataforma que conecta hogares salvadoreños con técnicos de confianza. Cada tipo de usuario tiene su propio panel: administrador, recepcionista, profesional y cliente.',
       screens=[('hog-1', 'Buscar profesionales por servicio y lugar'), ('hog-2', 'Registro de clientes y profesionales'), ('hog-adm-dash', 'Panel admin: resumen de profesionales, categorías y clientes'), ('hog-adm-sol', 'Panel admin: todas las solicitudes con su profesional asignado'), ('hog-adm-4', 'Panel admin: aprobar o rechazar pagos por transferencia'), ('hog-pro-trabajos', 'Panel profesional: bolsa de trabajo con solicitudes para cotizar'), ('hog-pro-billetera', 'Panel profesional: billetera con saldo y comisiones'), ('hog-pro-perfil', 'Panel profesional: perfil verificado con reseñas y cuenta bancaria')],
       admin=[
         ('Aprobar profesionales', 'Revisar cada registro, editar perfiles y ver el historial de trabajos de cada técnico.'),
         ('Seguir las solicitudes', 'Ver cada trabajo de principio a fin y su estado.'),
         ('Organizar los servicios', 'Categorías, especialidades, clientes y residenciales.'),
         ('Controlar las finanzas', 'Comisiones, verificación de pagos, pagos a profesionales, cuentas bancarias e historial.'),
         ('Atender y dar soporte', 'Reportes, atención por WhatsApp y solicitudes para eliminar cuentas.'),
       ]),
  dict(id='be', name='be.', sub='Tienda de activewear', url='https://beoficial.com', label='beoficial.com',
       color='#D1AA99', ink='#5B3A2E', tags=['Ecommerce', 'Moda'],
       intro='Tienda en línea de activewear con marcas como DFYNE y Gymshark, organizada por líneas de producto, con cuentas de cliente y seguimiento de compras.',
       screens=[('be-1', 'Catálogo por marca y por línea'), ('be-3', 'Creación de cuenta del cliente')],
       admin=[
         ('Administrar el catálogo', 'Productos por marca y por línea (Vision, Dynamic, Impact, Defy), con sus fotos y tallas.'),
         ('Recibir pedidos', 'Cada compra llega con los datos y la dirección de entrega del cliente.'),
         ('Conocer a sus clientes', 'Cuentas registradas con su historial de compras.'),
       ]),
  dict(id='finanzas', name='Finanzas Work', sub='Finanzas por proyecto', url='https://finanzas.work', label='finanzas.work',
       color='#1F4D3A', ink='#123326', tags=['Web app', 'Finanzas', 'Equipos'],
       intro='App para llevar el dinero separado por proyecto: el negocio, lo personal y los ahorros, cada uno con sus cuentas.',
       screens=[('fin-app-1', 'Saldo total, lo que entró y salió, y anotar un gasto escribiendo'), ('fin-app-2', 'Movimientos del mes y en qué se fue el dinero'), ('fin-app-3', 'Plan de ahorro con metas y lo que te deben')],
       admin=[
         ('Separar el dinero por proyecto', 'Cada negocio, gasto personal o meta tiene su propio saldo.'),
         ('Anotar como hablas', 'Escribes “gasté $20 de gas” y la app registra el movimiento y elige la categoría.'),
         ('Trabajar en equipo', 'Invitar a un socio o contador con un enlace y darle un rol: dueño, administrador, miembro o solo lectura.'),
         ('Controlar permisos', 'Cada rol define quién puede ver o editar.'),
         ('Revisar la actividad', 'Un historial muestra quién hizo cada cambio.'),
       ]),
]

e = html.escape
ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
BACK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'
NEXT = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
LOGO = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 3h9a8 8 0 0 1 0 16H9v-5h4a3 3 0 0 0 0-6H9v3H4z"/><path d="M4 16h4v5H4z"/></svg>'


def pagina(p):
    def titulo(cap):
        tag = ''
        for pref in ('Panel admin', 'Panel profesional'):
            if cap.startswith(pref + ': '):
                tag, cap = pref, cap[len(pref) + 2:]
                cap = cap[0].upper() + cap[1:]
        etiqueta = f'<span class="tag">{e(tag)}</span>' if tag else ''
        return etiqueta, cap
    shots = '\n'.join(
        (lambda t: f'<figure class="shot"><figcaption>{t[0]}<span class="cap">{e(t[1])}</span></figcaption><img src="../img/screens/{s}.jpg" alt="{e(t[1])}" width="390" height="844" loading="{"eager" if i < 3 else "lazy"}"></figure>')(titulo(cap))
        for i, (s, cap) in enumerate(p['screens']))
    admin = '\n'.join(f'<li><b>{e(t)}</b><span>{e(d)}</span></li>' for t, d in p['admin'])
    tags = ''.join(f'<span>{e(t)}</span>' for t in p['tags'])
    otros = '\n'.join(
        f'<a class="other" href="{o["id"]}.html"><img src="../img/logos/{o["id"]}.png" alt="" width="52" height="52"><span><b>{e(o["name"])}</b><small>{e(o["sub"])}</small></span></a>'
        for o in PROYECTOS if o['id'] != p['id'])
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['name'])} — Diego</title>
<meta name="description" content="{e(p['intro'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Inter+Tight:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="proyecto.css">
<style>:root{{--p:{p['color']};--pink:{p['ink']}}}</style>
</head>
<body>
<header class="top">
  <div class="wrap top-in">
    <a class="back" href="../index.html#proyectos">{BACK}<span>Proyectos</span></a>
    <a class="logo" href="../index.html" aria-label="Diego, inicio">{LOGO}Diego</a>
  </div>
</header>

<main class="wrap">
  <section class="app-head">
    <img class="icon" src="../img/logos/{p['id']}.png" alt="Logo de {e(p['name'])}" width="128" height="128">
    <div class="meta">
      <h1>{e(p['name'])}</h1>
      <p class="sub">{e(p['sub'])}</p>
      <div class="tags">{tags}</div>
    </div>
    <div class="actions">
      <a class="btn dark" href="{p['url']}" target="_blank" rel="noopener">Visitar {e(p['label'])}<i>{ARROW}</i></a>
      <a class="btn light" href="../index.html#contacto">Quiero algo así</a>
    </div>
  </section>

  <section class="gallery-wrap" aria-label="Vista previa">
    <div class="sec-title"><h2>Vista previa</h2>
      <div class="nav-btns"><button type="button" id="prev" aria-label="Anterior">{BACK}</button><button type="button" id="next" aria-label="Siguiente">{NEXT}</button></div>
    </div>
    <div class="gallery" id="gallery" tabindex="0">
{shots}
    </div>
  </section>

  <section class="about">
    <p>{e(p['intro'])}</p>
  </section>

  <section class="admin">
    <h2>Desde el panel administrativo puedes</h2>
    <ul>
{admin}
    </ul>
  </section>

  <section class="others">
    <h2>Otros proyectos</h2>
    <div class="other-list">
{otros}
    </div>
  </section>
</main>

<footer class="wrap foot"><span>© 2026 Diego · Desarrollo web y ecommerce</span><a href="../index.html#contacto">Hablemos</a></footer>

<script>
  const g = document.getElementById('gallery');
  const step = () => (g.querySelector('.shot')?.offsetWidth || 260) + 16;
  document.getElementById('prev').onclick = () => g.scrollBy({{left: -step(), behavior: 'smooth'}});
  document.getElementById('next').onclick = () => g.scrollBy({{left: step(), behavior: 'smooth'}});
</script>
</body>
</html>
'''


if __name__ == '__main__':
    out = RAIZ / 'proyectos'
    out.mkdir(exist_ok=True)
    for p in PROYECTOS:
        (out / f"{p['id']}.html").write_text(pagina(p), encoding='utf-8')
        print('ok', p['id'])
