from apps.messenger.components.attachments import TemplateAttachment, VideoAttachment
from apps.messenger.components.buttons import PostbackButton, LoginButton, URLButton
from apps.messenger.components.elements import ListElement, Element, ReceiptElement, ReceiptAddress, Summary, \
    Adjustment
from apps.messenger.components.messages import Message
from apps.messenger.components.requests import MessageRequest
from apps.messenger.components.templates import ListTemplate, GenericTemplate, ReceiptTemplate
from apps.messenger.components.replies import QuickReplies, TextReply, LocationReply
from apps.messenger.samples.responses import Components
from apps.messenger.motos import constants
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import urllib.request,json
import random

from apps.producto.models import Producto
from apps.propaganda.models import Propaganda

def _get_clima():
    with urllib.request.urlopen("http://api.geonames.org/findNearByWeatherJSON?lat=-16.49572&lng=-68.13346&username=eduardo_gpg") as url:
        data = json.loads(url.read().decode('utf-8'))
        temperature = data["weatherObservation"]["temperature"]
        humidity = data["weatherObservation"]["humidity"]
        return temperature, humidity

class RepliesMixin(object):

    def __init__(self, event, messenger):
        self.event = event
        self.messenger =  messenger

    def typing(self):
        responses = list()
        responses.append(MessageRequest(self.event.sender, sender_action='mark_seen'))
        responses.append(MessageRequest(self.event.sender, sender_action='typing_on'))
        self.messenger.post_message_queue(responses)
        
    def render_clima(self):
        temperature,humidity = _get_clima()
        self.typing()
        responses = list()

        message = Message(
        text =" 🙂 Nos encontramos a {}ºC  de Temperatura y {}%  de Humedad 👈 ".format(temperature,humidity),
        )

        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_usmbot(self):
        self.typing()
        responses = list()

        message = Message(
            text="Usmbot – tu amigo digital es un asistente en línea, a través del Messenger de Facebook. \n"
                 "Sera un gusto hablar contigo 🙂  🔧 👍.",
            )

        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_saludo(self):
        self.typing()
        responses = list()

        message = Message(
            text="⭐ Hola que tal \n"
                 "me llamo USMBOT soy tu asistente virtual 🙂  🔧 👍.",
            )

        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_chiste(self):
        self.typing()
        responses = list()

        chiste = dict()

        chiste = {
                'titulo0':'Motocicletas', 'chiste0':'A QUE NO SABÉIS QUIÉN FUE EL PRIMER MOTORISTA DE LA HISTORIA????????? , DAVID, PORQUE MATÓ A GOLIAT CON UNA HONDA',
                'titulo1':'Tonto Tonto', 'chiste1':'Era un señor tan tonto, tan tonto, tan tonto, que vendió la moto para comprar gasolina.',
                'titulo2':'¿Cuál es el colmo de un motociclista?', 'chiste2':'El que saque la mano para ver si esta lloviendo.',
                'titulo3':'¿Por qué a los hombres les gustan las motos y los autos?', 'chiste3':'Porque es lo único que pueden manejar.',
                'titulo4':'¿En qué se nota lo contento que va un motorista? ', 'chiste4':' En la cantidad de mosquitos que lleva en los dientes. ',
                'titulo5':' ¿Como se dice en árabe a una mujer "baja de la moto"? ', 'chiste5':' Baja la raja de la yamaha.',
                'titulo6':' Cual son los mejores motoristas de enduro de Japon:', 'chiste6':'Yoj Odolamoto y Yamimoto Nocarbura',
                'titulo7':'¿Cómo se llama ladrón de motos en japonés?', 'chiste7':'Yotekito lamoto',
                'titulo8':'Quiero tanto ami mujer que le puse ', 'chiste8':'Mercedez-Benz',
                'titulo9':'La marca de motos más Navideña', 'chiste9':'Ho Ho Ho Ho Ho Honda',
                'titulo10':'Yo no Ronco ', 'chiste10':'Sueño que soy una moto',
                'titulo11':'Van dos soldados en una moto', 'chiste11':'y nose caen porque van soldados',
                'titulo12':'Mi novia me dijo que elejiera entre la moto o ella', 'chiste12':'Aveces extraño a mi Novia xD',
                'titulo13':'Por qué las motos son mejores que las mujeres?', 'chiste13':'no se enojan cuando montas otras motos, puedes prestar la a tu amigo, puedes ver otras motos sin que te critique.',
                'titulo14':'Te caiste Amor?', 'chiste14':'No idiota estoy viendo si se salio la cadena',
                'titulo15':'¿Cuál es la diferencia entre un motor y un inodoro?', 'chiste15':' En que en el motor tu te sientas para correr, y en el inodoro tu corres para sentarte',
                'titulo16':'Coche viejo', 'chiste16':'Era un carro tan viejo, que cuando el conductor sacó la mano para virar, le dieron limosna',
                'titulo17':'¿Que hace un arbitro en el baño', 'chiste17':'......expulsar a Kaka',
                'titulo18':'Como maldice un pollito a otro pollito?', 'chiste18':'Caldito seas',
                'titulo19':'¿QUE HACE UNA VACA EN UNA CARRETERA?', 'chiste19':'VACA-MINANDO',
                'titulo20':'¿Cual es el país que ríe y explota ?', 'chiste20':'Ja - pón  xD',
                'titulo21':'Cual es el vino mas amargo?', 'chiste21':'VINO MI SUEGRA',
                'titulo22':'Que hace un perro con un taladro ?', 'chiste22':'Taladrando  jejeje ... ',
                'titulo23':'Que hace una vaca con los ojos cerrados', 'chiste23':'Leche concentrada :v',
                'titulo24':'¿Cuál es el colmo de un pianista? ', 'chiste24':'Que su mujer se llame tecla y la toque otro.',
                'titulo25':'¿por que la gente se suicida en los baños ? ', 'chiste25':'Por que la crema dental dice ( colgate ) :v',
                'titulo26':'Que pasa si cae una bomba al vaticano...', 'chiste26':'Pure de papa jajajaja '

        }

        key_random = random.randrange(25)

        _titulo = chiste['titulo'+str(key_random)]
        _chiste = chiste['chiste'+str(key_random)]

        message = Message(
            text="😜"+_titulo
            )
        responses.append(MessageRequest(self.event.sender, message))

        message = Message(
            text=_chiste+"😅",
            )

        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_start(self):

        self.typing()
        responses = list()

        message = Message(text="Tengo las siguientes opciones para tí.")
        responses.append(MessageRequest(self.event.sender, message))

        template = ListTemplate(
            elements=[
                ListElement(
                    title="USMOTOS",
                    image_url="https://goo.gl/5EGLWp",
                    subtitle="usmotos",
                    buttons=[
                        PostbackButton(
                            title="Conocer",
                            payload=constants.INFORMATION_BUSINESS
                        )
                    ],
                ),
                ListElement(
                    title="PRODUCTOS",
                    image_url="https://goo.gl/09oGyc",
                    subtitle="Motocicletas y Accesorios",
                    buttons=[
                        PostbackButton(
                            title="Ver",
                            payload=constants.SHOW_PRODUCTS
                        )
                    ],
                ),
            ]
        )
        attachment = TemplateAttachment(template=template)
        message = Message(attachment=attachment)
        responses.append(Components.typing(responses, self.event.sender))
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_products(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[
                TextReply(
                    image_url="https://goo.gl/wFPqYL",
                    title="MOTOCICLETAS",
                    payload=constants.SHOW_CATEGORY_MOTORCYCLE,
                ),

                TextReply(
                    image_url="https://goo.gl/gY5Kr9",
                    title="PROMOCIONES",
                    payload=constants.SHOW_PROMOTIONS,
                ),

                TextReply(
                    image_url="https://goo.gl/XuddLH",
                    title="ACCESORIOS",
                    payload=constants.SHOW_ACCESORIES,
                ),
                # LocationReply(), PARA LAS DIRECCIONES

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="CANCELAR",
                    payload=constants.CANCEL,
                ),
            ]
        )
        message = Message(
            text="¿que seleccionaras 😄?",
            quick_replies=replies
        )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_information(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[
                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="MISION",
                    payload=constants.MISSION,
                ),

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="VISION",
                    payload=constants.VIEW,
                ),

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="HORARIOS",
                    payload=constants.SCHEDULE,
                ),

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="DIRECCION",
                    payload=constants.ADDRESS,
                ),


                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="CANCELAR",
                    payload=constants.START,
                ),
            ]
        )
        message = Message(
            text="Aqui tienes informacion de la empresa 😄",
            quick_replies=replies
        )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_show_view(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="REGRESA",
                    payload=constants.INFORMATION_BUSINESS,
                ),

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="INICIO",
                    payload=constants.START,
                ),
            ]
        )

        message = Message(
            text="⭐ Empresa dedicada a ala distribucion y comercializacion de Motocicletas\n"
                 "Apoyados por un equipo 🙂 calificado con actitud de servicio y honestidad 🔧 👍.",
            quick_replies=replies
            )

        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_show_mission(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="REGRESA",
                    payload=constants.INFORMATION_BUSINESS,
                ),

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="INICIO",
                    payload=constants.START,
                ),
            ]
        )
        message = Message(
            text="😀 En el 2020 ser reconocido como empresa lider a nivel nacional 💡 ✅ en distribucion de Motocicletas\n"
                 "por la calidad y amplio portafolio y productos y servicios que ofrece.",
            quick_replies=replies
            )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_show_address(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="REGRESA",
                    payload=constants.INFORMATION_BUSINESS,
                ),

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="INICIO",
                    payload=constants.START,
                ),
            ]
        )
        message = Message(
            text="👉 c. Panamá esq. Brasil # 1590, La Paz, Bolivia 😎\n"
                 "📞 2115625 📱",
            quick_replies = replies
            )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_schedule(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="REGRESA",
                    payload=constants.INFORMATION_BUSINESS,
                ),

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="INICIO",
                    payload=constants.START,
                ),
            ]
        )
        message = Message(
            text="⌚ Abre a las 8:30 (8:30 - 12:30, 14:30 - 19:00) 🌞",
            quick_replies = replies
            )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_categorys_moto(self):
        elements = []

        self.typing()
        responses = list()

        text = TextReply(
                    title="NAKED",
                    image_url='https://goo.gl/62juy0',
                    payload=constants.NAKED,
                )
        elements.append(text)

        text = TextReply(
                    title="SCOOTER",
                    image_url='https://goo.gl/hrU5Uu',
                    payload=constants.SCOOTER,
                )
        elements.append(text)

        text = TextReply(
                    title="CRUCERO",
                    image_url='https://goo.gl/oYUSxA',
                    payload=constants.CRUCERO,
                )
        elements.append(text)

        text = TextReply(
                    title="CHOOPER",
                    image_url='https://goo.gl/HsG2Zu',
                    payload=constants.CHOOPER,
                )
        elements.append(text)

        text = TextReply(
                    title="CUSTOM",
                    image_url='https://goo.gl/WMAjzN',
                    payload=constants.CUSTOM,
                )
        elements.append(text)

        text = TextReply(
                    title="SIDECAR",
                    image_url='https://goo.gl/0YYM0c',
                    payload=constants.SIDECAR,
                )
        elements.append(text)

        text = TextReply(
                    title="TOURING",
                    image_url='https://goo.gl/dS0cqF',
                    payload=constants.TOURING,
                )
        elements.append(text)

        text = TextReply(
                    title="RACER",
                    image_url='https://goo.gl/PZz362',
                    payload=constants.RACER,
                )
        elements.append(text)

        text = TextReply(
                    title="TRIAL",
                    image_url='https://goo.gl/LXWy1a',
                    payload=constants.TRIAL,
                )
        elements.append(text)

        text = TextReply(
                    title="CANCELAR",
                    image_url="https://goo.gl/oY50Tk",
                    payload=constants.CANCEL,
                )
        elements.append(text)

        numbers = QuickReplies(
            replies=elements
        )

        message = Message(
            text="Categorias",
            quick_replies=numbers
        )

        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_naked(self):
        self.typing()

        motos_naked = Producto.objects.all().filter(tipo = "Naked")

        _naked = 0

        for m_active in motos_naked:
            if m_active.habilitado == True and m_active.tipo == "Naked":
                _naked +=1 

        print("CANTIDAD NAKED", _naked)

        list_url_motos = [
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb',
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
        ]

        responses = list()
        elements = []

        if _naked > 0 and _naked <= 10:
            message = Message(text="Tenemos las soguientess motocicletas de Tipo Nacked", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1

            for naked in motos_naked:
                if naked.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if naked.habilitado == True:
                    element = Element(
                        title=naked.nombre,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(naked.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
            
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Naked registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_show_moto_scooter(self):
        self.typing()

        motos_scooter = Producto.objects.all().filter(tipo = "Scooter")

        _scooter = 0

        for m_active in motos_scooter:
            if m_active.habilitado == True and m_active.tipo == "Scooter":
                _scooter +=1 

        print("CANTIDAD SCOOTER", _scooter)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _scooter > 0 and _scooter <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Scooter", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for scooter in motos_scooter:
                if scooter.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if scooter.habilitado == True:
                    element = Element(
                        title=scooter.nombre,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(scooter.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Scooter registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_crucero(self):
        self.typing()

        motos_crucero = Producto.objects.all().filter(tipo = "Crucero")

        _crucero = 0

        for m_active in motos_crucero:
            if m_active.habilitado == True and m_active.tipo == "Crucero":
                _crucero +=1 

        print("CANTIDAD CRUCERO", _crucero)

        list_url_motos = [
            'https://goo.gl/y3Hym7',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/76utQ6',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/knZMpb',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/opMbeu',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/GdgDbF',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/Q7799l',
            'https://goo.gl/09oGyc'
        ]

        responses = list()
        elements = []

        if _crucero > 0 and _crucero <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Crucero", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for crucero in motos_crucero:
                if crucero.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if crucero.habilitado == True:
                    element = Element(
                        title=crucero.nombre,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(crucero.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Crucero registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_show_moto_chooper(self):
        self.typing()

        motos_chooper = Producto.objects.all().filter(tipo = "Chooper")

        _chooper = 0

        for m_active in motos_chooper:
            if m_active.active == True and m_active.tipo == "Chooper":
                _chooper +=1 

        print("CANTIDAD CHOOPER", _chooper)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _chooper > 0 and _chooper <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Chooper", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for chooper in motos_chooper:
                if chooper.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if chooper.habilitado == True:
                    element = Element(
                        title=chooper.nombre,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(chooper.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Custom registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_custom(self):
        self.typing()

        motos_custom = Producto.objects.all().filter(tipo = "Custom")

        _custom = 0

        for m_active in motos_custom:
            if m_active.active == True and m_active.tipo == "Custom":
                _custom +=1 

        print("CANTIDAD CUSTOM", _custom)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _custom > 0 and _custom <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Custom", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for custom in motos_custom:
                if custom.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if custom.habilitado == True:
                    element = Element(
                        title=custom.nombre,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(custom.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Custom registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_sidecar(self):
        self.typing()

        motos_sidecar = Producto.objects.all().filter(tipo = "Sidecar")

        _sidecar = 0

        for m_active in motos_sidecar:
            if m_active.active == True and m_active.tipo == "Sidecar":
                _sidecar +=1 

        print("CANTIDAD SIDECAR", _sidecar)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _sidecar > 0 and _sidecar <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Sidecar", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for sidecar in motos_sidecar:
                if sidecar.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if sidecar.habilitado == True:
                    element = Element(
                        title=sidecar.nombre,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(sidecar.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Sidecar registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_touring(self):
        self.typing()

        motos_touring = Producto.objects.all().filter(tipo = "Touring")

        _touring = 0

        for m_active in motos_touring:
            if m_active.habilitado == True and m_active.tipo == "Touring":
                _touring +=1 

        print("CANTIDAD TOURING", _touring)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _touring > 0 and _touring <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Touring", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for touring in motos_touring:
                if touring.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if touring.habilitado == True:
                    element = Element(
                        title=touring.nombre,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(touring.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Touring registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_racer(self):
        self.typing()

        motos_racer = Producto.objects.all().filter(tipo = "Racer")

        _racer = 0

        for m_active in motos_racer:
            if m_active.habilitado == True and m_active.tipo == "Racer":
                _racer +=1 

        print("CANTIDAD RACER", _racer)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _racer > 0 and _racer <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Racer", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for racer in motos_racer:
                if racer.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if racer.habilitado == True:
                    element = Element(
                        title=racer.nombre,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(racer.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Racer registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_trial(self):
        self.typing()

        motos_trial = Producto.objects.all().filter(tipo = "Trial")

        _trial = 0

        for m_active in motos_trial:
            if m_active.habilitado == True and m_active.tipo == "Trial":
                _trial +=1 

        print("CANTIDAD TRIAL", _trial)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _trial > 0 and _trial <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Trial", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for trial in motos_trial:
                if trial.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if trial.habilitado == True:
                    element = Element(
                        title=trial.nombre,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(trial.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Trial registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_promotions(self):
        self.typing()

        promociones = Propaganda.objects.all().filter(habilitado = True)

        responses = list()
        elements = []

        if promociones.count() > 0 and promociones.count() <= 10:
            message = Message(text="😀 Estas son promociones que tenemos para ti 🎁 ", )
            responses.append(MessageRequest(self.event.sender, message))

            for promocion in promociones:
                if promocion.habilitado == True:
                    element = Element(
                        title=promocion.nombre,
                        image_url="https://goo.gl/OQGTtF",
                        subtitle="USM - PROMOCIONES",
                        buttons=[
                            URLButton(
                                title="VER DETALLE",
                                url=promocion.url
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Contarte que no hay Promociones Habilitadas 😱, estate atento pronto habra promociones 😉 👍 ",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_accesories(self):
        self.typing()

        accesorios = Producto.objects.all().filter(tipo = "Accesorio")

        _accesorio = 0

        for m_active in accesorios:
            if m_active.habilitado == True and m_active.tipo == "Accesorio":
                _accesorio +=1 

        print("CANTIDAD ACCESORIOS ", _accesorio)

        responses = list()
        elements = []

        if _accesorio > 0 and _accesorio <= 10:
            message = Message(text="Aqui te muestro los Accesorios", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for accesorio in accesorios:
                if accesorio.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if accesorio.habilitado == True:
                    element = Element(
                        title=accesorio.nombre,
                        image_url="https://goo.gl/vhWQE5",
                        subtitle='{}-{}'.format(accesorio.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay accesorios disponibles",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_process_user(self):
        responses = list()
        self.typing()

        if hasattr(self, "player_added"):
            text = self.player_added + " es invalido vuelve a intentarlo"
        else:
            text = "Porfavor ingresa tu Cedula de Identidad"

        replies = QuickReplies(
            replies=[
                TextReply(
                    image_url="https://goo.gl/6t7mb7",
                    title="CANCELAR",
                    payload=constants.START_DESTROY,
                ),

            ]
        )
        message = Message(
            text=text,
            quick_replies=replies
        )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_list_asistencias(self):
        self.typing()

        _user = self.session["store"]["users_ci"]

        print("user ", _user)
        print("type ", type(_user))

        for x in _user:
            _select_id = x['ci']

        _select_id = int(_select_id)

        asistencias = Asistencia.objects.all().filter(habilitado = True)

        contador = 0
        for asistencia in asistencias:
            if _select_id == int(asistencia.cliente.cedula):
                contador +=1


        print("CONTADOR ", contador)


        responses = list()
        elements = []

        if contador > 0 and contador <= 10:
            message = Message(text="Hola 😄 aqui esta el listado de tus asistencias ", )
            responses.append(MessageRequest(self.event.sender, message))

            for asistance in asistencias:
                if _select_id == int(asistance.cliente.cedula) and asistance.estado_reparacion == "PENDIENTE":
                    element = Element(
                        title=asistance.placa.upper(),
                        image_url="https://goo.gl/7c63UD",
                        subtitle="Devolucion "+ str(asistance.fecha_salida),
                        buttons=[
                            PostbackButton(
                                title="TERMINAR",
                                payload=constants.START_DESTROY
                            ),
                            PostbackButton(
                                title="VOLVER A CONSULTAR",
                                payload=constants.ADD_CEDULA_DESTROY
                            ),
                        ]
                    )
                    elements.append(element)
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="No se pudo mostrar Asistencia Mecanica 😱",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_login(self):
        template = GenericTemplate(
            elements=[
                Element(
                    title="Iniciar Sesión",
                    subtitle="y Que siga la Fiesta",
                    buttons=[
                        LoginButton(
                            url=self.get_url("/facebook/authorize/%s/" % self.event.sender.id)
                        )
                    ]
                )
            ]
        )

        attachment = TemplateAttachment(template=template)
        message = Message(attachment=attachment)
        response =  MessageRequest(self.event.sender, message)
        self.messenger.post_message(response)


    def render_logged_in(self):
        responses = list()
        message = Message(text=" Login con Exito 😄")
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_message(self, text):
        self.typing()
        responses = list()
        message = Message(text=text)
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

# ----------------------------------------------------------------------


    def render_category_list(self):
        # responses = list()
        # message = Message(text="Escribe que tipo de bebida")
        # responses.append(Components.typing(responses, self.event.sender))
        # responses.append(MessageRequest(self.event.sender, message))
        pass



