from django.db import models

class RegistroU(models.Model):
    id_registroU = models.IntegerField(primary_key=True, db_column='idGenero')
    nombre = models.CharField(max_length=100, db_column='nombre')
    apellidop = models.CharField(max_length=100, db_column='apellidoP')
    apellidom = models.CharField(max_length=100, db_column='apellidoM')
    email = models.CharField(max_length=50, db_column='email')
    contra = models.CharField(max_length=100, db_column='contra')
    class Meta:
        db_table='R_usuario'

class Encuesta(models.Model):
    id_respuesta = models.IntegerField(primary_key=True, db_column='idRespuesta')
    gama = models.CharField(max_length=15, db_column='gama')
    frecuencia = models.CharField(max_length=30, db_column='frecuencia')
    met_pago = models.CharField(max_length=30, db_column='met_pago')
    dispositivo = models.CharField(max_length=30, db_column='dispositivo')
    opc_correo = models.CharField(max_length=10, db_column='opc_correo')
    serv_mensajeria = models.CharField(max_length=30, db_column='serv_mensajeria')
    opc_chatbot = models.CharField(max_length=10, db_column='opc_chatbor')
    opc_atencion_pers = models.CharField(max_length=10, db_column='opc_atencion_pers')
    tiempo_nave = models.CharField(max_length=50, db_column='tiempo_nav')
    class Meta:
        db_table='respuesta'
