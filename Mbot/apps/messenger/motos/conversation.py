import json
import re

from datetime import datetime

from transitions import Machine

from django.core.cache import cache

from apps.messenger.motos import constants
from apps.messenger.motos.contexts import ContextMixin
from apps.messenger.motos.responses import RepliesMixin
from apps.messenger.motos.conditions import ConditionsMixin
from apps.messenger.motos.utils import UtilsMixin


class CacheSession(object):
    @staticmethod
    def put(sender_id, state):
        cache.set(sender_id, json.dumps(state))

    @staticmethod
    def get(sender_id):
        if cache.get(sender_id) is None:
            state = {
                "trace": [], "state": "", "store": {},
                "update": str(datetime.now())
            }
            cache.set(sender_id, json.dumps(state))
        else:
            state = json.loads(cache.get(sender_id))

        return state

    @staticmethod
    def reset(sender_id, state, store):
        state = {
            "trace": [],"state": "", "store": {}
        }
        cache.set(sender_id, json.dumps(state))
        return state




class Conversation(UtilsMixin, RepliesMixin, ConditionsMixin, ContextMixin):

    states = constants.states
    transitions = constants.transitions

    @property
    def triggers(self):
        items = list()
        for transition in self.transitions:
            items.append(transition['trigger'])
        return items


    def __init__(self, event, messenger):
        super(Conversation, self).__init__(event, messenger)
        self.machine = Machine(
            model=self,
            transitions=Conversation.transitions,
            states=Conversation.states, 
            initial=constants.START,
            # ignore_invalid_triggers=True
        )

        self.session = CacheSession.get(event.sender.id)

        # This regenerate state
        if self.session["state"] and self.session["state"] in self.states:
            self.machine.set_state(self.session["state"], self)

        self.set_environment()

    def set_environment(self, valid_phone=False, valid_pin=False):
        self.valid_phone = valid_phone
        self.valid_pin = valid_pin

    def save(self):
        self.session["state"] = self.state
        CacheSession.put(self.event.sender.id, self.session)

    def reset(self):
        self.session["store"] = dict()
        self.session["state"] = self.state
        CacheSession.reset(self.event.sender.id, self.session, self.session)


def generate_response(event, messenger):
    # print(event)
    conversation = Conversation(event, messenger)

    if event.is_message:
        print("\n", "---> ES MESSAGE < ---", event.data)
  
        mensaje = event.data['_message']
        _message = mensaje['text']
        print(">>>>>>>>># ", _message)

        if _message.find("hola")>=0 or _message.find("Hola")>=0:
            conversation.render_saludo()

        elif _message.find("clima")>=0 or _message.find("Clima")>=0:
            conversation.render_clima()

        elif _message.find("usmbot")>=0 or _message.find("Usmbot")>=0:
            conversation.render_usmbot()

        elif _message.find("chiste")>=0 or _message.find("Chiste")>=0:
            conversation.render_chiste()


        elif conversation.state != constants.START:
            conversation.listen_values()

        else:
            conversation.render_start()

    elif event.is_postback:
        payload = conversation.process_payload(event.payload)
        print("el payload >> ", payload)

        if payload in conversation.triggers:
            try:
                conversation.trigger(payload)
            except Exception as e:
                print("ERROR: ",e)
                getattr(conversation, 'render_' + conversation.state)()


        if payload  == constants.START_DESTROY:
            print("RESET CACHE")
            conversation.reset()

        if payload  == constants.ADD_CEDULA_DESTROY:
            print("RESET CACHE")
            conversation.reset()


        print("\n  ES POSTBACK >>$ ", payload)

        if payload == "FACEBOOK_WELCOME":
            conversation.render_saludo()

    elif event.is_quick_reply:
        payload = conversation.process_payload(event.payload)
        print("el payload >> ", payload)

        print("\n", "---> QUICK REPLY < ---")
        if event.payload:
            try:
                conversation.trigger(event.payload)
            except Exception as e:
                print("ERROR: ",e)
                getattr(conversation, 'render_' + conversation.state)()

        if payload  == constants.START_DESTROY:
            print("RESET CACHE")
            conversation.reset()

    elif event.is_delivery:
        pass
        # print("\n", "---> ES ENTREGABLE < ---")
    elif event.is_read:
        pass
        # print("\n", "---> ES UN MENSAJE LEIDO < ---")
        
    elif event.is_authentication:
        print("\n", "---> ES AUTENTICACIÓN < ---")

    elif event.is_account_linking:
        print("\n", "---> ACCOUNT_LINKING < ---")

        if event.account_linking:
            print("El evento ", event.account_linking)
            status_acl = event.account_linking.get("status")

            if status_acl == 'linked':
                print("\n", "---> ES VINCULACION DE CUENTAS < ---", "\n")
                


    elif event.is_referral:
        print("\n", "---> ES REFERIDO < ---")
    elif event.is_checkout_update:
        print("\n", "---> ES CHECKOUT < ---")

    conversation.save()

    if event.is_message or event.is_postback or event.is_quick_reply or event.is_account_linking:
        print("\n-------------------------------->>>>> state >> ", conversation.state)
        print("\n**********************************************************")
        print("\n", conversation.session)
        print("\n**********************************************************")

