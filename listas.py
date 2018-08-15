from comandos import *
from eventos import *
from tareas import *

coms = {
	"ping": ping.ping,
	#Moderación
	#silencio
	"mute": silencio.mute,
	"silenciar": silencio.mute,
	"silencia": silencio.mute,
	"unmute": silencio.unmute,
	"desilenciar": silencio.unmute,
	"desilencia": silencio.unmute,
	#expulsión
	"ban": ban.ban,
	"excluir": ban.ban,
	"kick": ban.ban,
	"desbanear": ban.unban,
	"unban": ban.unban,
	#Mix
	"reverse": mix.reverso,
	"reverso": mix.reverso, #alias
	"reves": mix.reverso, #alias
	"revés": mix.reverso, #alias
	"decir": mix.decir,
	"say": mix.decir, #alias
	"di": mix.decir, #alias
	"elegir": mix.elegir,
	"choose": mix.elegir, #alias
	"elige": mix.elegir, #alias
	#AVATAR
	"avatar": mix.obtener_avatar,
	#Democracia
	"democracia": democracia.maneja_encuestas,
	"vota": democracia.maneja_encuestas,
	"vote": democracia.maneja_encuestas,
	"encuesta": democracia.maneja_encuestas,
	"poll": democracia.maneja_encuestas,
	"votacion": democracia.maneja_encuestas,
	"votar": democracia.maneja_encuestas,
	#Prefijos
	"prefix": prefijos.maneja_prefijos,
	"prefijo": prefijos.maneja_prefijos,
	"prefijos": prefijos.maneja_prefijos,
	"prefixes": prefijos.maneja_prefijos,
	#Nicks
	"nick": nicks.manejar_apodos,
	"nicks": nicks.manejar_apodos,
	"setnick": nicks.manejar_apodos,
	"apodos": nicks.manejar_apodos,
	"apodo": nicks.manejar_apodos,
	#Roles
	"rol": roles.toggle_roles,
	"role": roles.toggle_roles,
	"roles": roles.toggle_roles,
	#Destacados
	"dcanal": destacados.canal_destacado,
	"dchannel": destacados.canal_destacado,
	"demoji": destacados.emoji_destacado,
	"dreaccion": destacados.emoji_destacado,
	"dreaction": destacados.emoji_destacado,
	"dminimo": destacados.minimo_destacado,
	"dminimum": destacados.minimo_destacado,
	"dmin": destacados.minimo_destacado,
	"dcrear": destacados.crear_tabla,
	"dvaciar": destacados.vaciar_tabla,
	#Confiables
	"confiable": confiables.confiables,
	"confiables": confiables.confiables,
	"conf": confiables.confiables,
	"confi": confiables.confiables,
	"confia": confiables.confiables,
	"confio": confiables.confiables,
	#Ayuda
	"ayuda": ayuda.ayuda_manejador,
	"help": ayuda.ayuda_manejador,
	"comandos": ayuda.ayuda_manejador,
	"commands": ayuda.ayuda_manejador,
	#Juegos
	"truco": cartas.dar_carta,
	#Cerrar
	"ciérrate sésamo": cerrar.cerrar,
	"close": cerrar.cerrar,
	"cerrar": cerrar.cerrar
}

evs = {
	"entra_miembro": [entra_miembro.silencio_entrar, 
					entra_miembro.roles_superduperserver],
	"entra_servidor": [entra_servidor.servidor_entro],
	"por_mensaje": [por_mensaje.procesar_comandos],
	"pone_reaccion": [en_reacciones.pone_destacados],
	"quita_reaccion": [en_reacciones.quita_destacados],
	"en_edicion": [en_ediciones.editar_destacados],
	"en_error": [en_error.maneja_errores]
}

tasks = [auto_silencio.auto_unmute]