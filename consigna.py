#Alertas de una plataforma educativa. El sistema necesita enviar
#alertas a los estudiastes sobre cargas de notas. Podemos usar e-mail, sms,
#pero tmabien podes usar notificaciones de push o por telegram mas adelantes.
#

from abc import ABC, abstractmethod
class CanalNotificacion(ABC):
    @abstractmethod
    def enviar_alerta(self, destinatario:str, mensaje:str):
        pass

class Email(CanalNotificacion):
    def enviar_alerta(self, destinatario:str, mensaje:str):
        print(f"Enviando email a {destinatario}: {mensaje}")
    
class SMS(CanalNotificacion):
    def enviar_alerta(self, destinatario, mensaje):
        print(f"Enviando SMS a {destinatario}: {mensaje}")
Alerta_mail = Email()
Alerta_mail.enviar_alerta("Juan@gmail.com","Desaprobaste.")

Alerta_SMS = SMS()
Alerta_SMS.enviar_alerta("222-55543","Puto el que lo lea")

def alerta_comunidad(lista_canales:list[CanalNotificacion], usuario:str, text:str):
    for canal in lista_canales:
        canal.enviar_alerta(usuario, text)

canales = [Email(), SMS()]
alerta_comunidad(canales, "Todos", "Tu nota ha sido cargada.")
 