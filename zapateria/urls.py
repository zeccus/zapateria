from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','principal.views.lista_zapatos'),
    url(r'^proovedores/$','principal.views.lista_proovedores'),
    url(r'^producto/(?P<id_zapato>\d+)$','principal.views.zapato_especifico',name = 'principal_productos'),
    url(r'^ninos/$','principal.views.zapato_nino', name = 'ninos'),
    url(r'^ninas/$','principal.views.zapato_nina',name = 'ninas'),
    url(r'^unisex/$','principal.views.zapato_unisex', name = 'uni'),
    url(r'^marcas/$','principal.views.marca'),
    url(r'^marca_producto/(?P<id_marca>\d+)$','principal.views.zapato_marca',name = 'principal_marcas'),
    url(r'^tipo/$','principal.views.tipo'),
    url(r'^tipo_zapato/(?P<id_tipo>\d+)$','principal.views.tipo_zapato',name = 'principal_tipos'),
    url(r'^marcas/nino/(?P<id_marca>\d+)$','principal.views.zapato_marcanino',name = 'ninomarca'),
    url(r'^marcas/nina/(?P<id_marca>\d+)$','principal.views.zapato_marcanina',name = 'ninamarca'),
    url(r'^marca/unisex/(?P<id_marca>\d+)$','principal.views.zapato_marcauni',name = 'unimarca'),
    url(r'^tipo_zapato/nino/(?P<id_tipo>\d+)$','principal.views.zapato_tiponino',name = 'ninotipo'),
    url(r'^tipo_zapato/nina/(?P<id_tipo>\d+)$','principal.views.zapato_tiponina',name = 'ninatipo'),
    url(r'^tipo_zapato/unisex/(?P<id_tipo>\d+)$','principal.views.zapato_tipouni',name = 'unitipo'),
    url(r'^contacto/$','principal.views.tienda'),
    url(r'^sobregarabatos/$','principal.views.garabatos'),
    url(r'^contactoform/$','principal.views.contacto'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
{'document_root':settings.MEDIA_ROOT,}),

) 
