from rest_framework.views import APIView
from rest_framework.response import Response

from apps.producto.models import Producto
from apps.proveedor.models import Proveedor
from apps.venta.models import DetalleVenta, Venta
from django.db.models import Q, Count, Sum
from django.db.models.functions import Coalesce
import datetime

class ChartProveedores(APIView):

    def get(self, request, format=None):

        productos = Producto.objects.all()

        proveedores = productos.values("proveedor").annotate(usados=Count('proveedor')).order_by(Coalesce('usados', 'usados').desc())

        for m in proveedores:
            m['proveedor'] = str(Proveedor.objects.get(id=m["proveedor"]).nombre)

        labels = list()
        default_items = list()

        for i in proveedores:
        	labels.append(i['proveedor'])  
        	default_items.append(i['usados'])

        data = {
                "Titulo": labels,
                "ProveedoresUsados": default_items,
        }
        return Response(data)



class ChartVentaProductos(APIView):

    def get(self, request, format=None):

        ventas = DetalleVenta.objects.all()

        _ventas = ventas.values("producto").annotate(usados=Count('producto')).order_by(Coalesce('usados', 'usados').desc())

        for m in _ventas:
            m['producto'] = str(Producto.objects.get(id=m["producto"]).nombre)

        labels = list()
        default_items = list()

        for i in _ventas:
            labels.append(i['producto'])  
            default_items.append(i['usados'])

        data = {
                "Titulo": labels,
                "ProductosVendidos": default_items,
        }
        return Response(data)


class ChartVentaProductosMes(APIView):

    def get(self, request, format=None):
        from datetime import date
        _today = date.today()

        _year = _today.year

        labels = list()
        default_items = list()
        _mes = ""

        for x in range(12):
            if x == 1:
                _month = 1
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Enero"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 2:
                _month = 2
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Febrero"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 3:
                _month = 3
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Marzo"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 4:
                _month = 4
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Abril"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 5:
                _month = 5
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Mayo"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 6:
                _month = 6
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Junio"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 7:
                _month = 7
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Julio"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 8:
                _month = 8
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Agosto"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 9:
                _month = 9
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Septiembre"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 10:
                _month = 10
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Octubre"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 11:
                _month = 11
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Noviembre"
                labels.append(_mes)
                default_items.append(_ventasmes)

            if x == 12:
                _month = 12
                _date = datetime.date(_year,_month,12)
                _ventasmes = Venta.objects.filter(fecha__month=_date.month).count()
                _mes = "Diciembre"
                labels.append(_mes)
                default_items.append(_ventasmes)

        data = {
                "Titulo": labels,
                "ProductosVendidos": default_items,
        }
        return Response(data)
