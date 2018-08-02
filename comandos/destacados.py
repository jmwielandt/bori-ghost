import os
import discord
import psycopg2
from emoji import UNICODE_EMOJI
from variables import tabla_destacados

async def canal_destacado(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	BD_URL = os.getenv("DATABASE_URL")
	base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
	bd = base_de_datos.cursor()
	bd.execute(tabla_destacados)
	bd.execute("SELECT id_canal FROM destacados")
	canal_destacados = bd.fetchone()
	if len(message.channel_mentions) > 0:
		if canal_destacados == None:
			await client.send_message(message.channel, "No han seleccionado ningún canal para mensajes destacados.")
		else:
			canalDestacado = discord.utils.get(message.server.channels, id = canal_destacados)
			await client.send_message(message.channel, "El canal para mensajes destacados es: "+canalDestacado.mention)
	elif mensaje_separado[1] in {"set", "pon", "en", "aquí", "aqui", "seleccionar", "choose"}:
		if not message.author.server_permissions.manage_channels:
			error = "¡Todo listo! Espera... Tú no tienes permisos para hacer eso. Mejor cómprate una MAC, {}."
			await client.send_message(message.channel, error.format(nick_autor))
		if len(message.channel_mentions) > 1:
			await client.send_message(message.channel, "ERROR: Tienes que elegir un solo canal.")
			return
		else:
			canal_agregar = message.channel_mentions[0]
			exito = "Has elegido el canal {} para los mensajes destacados"
			if canal_destacados == None:
				estrella = "⭐"
				agregar_bd = "INSERT INTO destacados(id_canal, emoji, minimo) VALUES(%s, %s, %s)"
				bd.execute(agregar_bd,(canal_agregar.id,estrella,1))
			else:
				bd.execute("UPDATE destacados SET id_canal = %s WHERE id_canal = %s", (canal_agregar.id, canal_destacados.id))
			await client.send_message(message.channel, exito.format(canal_agregar.mention))
			base_de_datos.commit()
	bd.close()
	base_de_datos.close()

async def emoji_destacado(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	emojis = [str(emoji) for emoji in message.server.emojis]
	emojis += UNICODE_EMOJI
	BD_URL = os.getenv("DATABASE_URL")
	base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
	bd = base_de_datos.cursor()
	bd.execute(tabla_destacados)
	bd.execute("SELECT emoji FROM destacados")
	emoji_destacados = bd.fetchone()
	if len(mensaje_separado) < 2:
		if emoji_destacados == None:
			await client.send_message(message.channel, "No se ha seleccionado ningún emoji para mensajes destacados.")
		else:
			await client.send_message(message.channel, "Ya puedes destacar mensajes con el emoji: "+emoji_destacados)
	elif len(mensaje_separado) > 3:
		await client.send_message(message.channel, "Dime sólo el emoji, no me cuentes tu vida.")
	elif mensaje_separado[1] in emojis:
		if message.author.server_permissions.manage_channels or message.author.server_permissions.manage_messages:
			if emoji_destacados == None:
				bd.execute("INSERT INTO destacados(emoji) VALUES(%s)", (mensaje_separado[1],))
			else:
				bd.execute("UPDATE destacados SET emoji = %s WHERE emoji = %s", (mensaje_separado[1], emoji_destacados))
			await client.send_message(message.channel, "Ya puedes reaccionar con "+mensaje_separado[1]+" para destacar mensajes.")
			base_de_datos.commit()
		else:
			await client.send_message(message.channel, "Ni lo creas, no tienes permiso de eso. No encenderé mi MAC por ti.")
	else:
		await client.send_message(message.channel, "Mira chico, estoy ocupado con mi juego de Star Wars, "+
														"así que no me molestes. Háblame cuando tengas el emoji.")
	bd.close()
	base_de_datos.close()

async def minimo_destacado(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	BD_URL = os.getenv("DATABASE_URL")
	base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
	bd = base_de_datos.cursor()
	bd.execute(tabla_destacados)
	bd.execute("SELECT minimo FROM destacados")
	minimo_destacados = bd.fetchone()
	if len(mensaje_separado) < 2:
		if minimo_destacados == None:
			await client.send_message(message.channel, "No se ha establecido la cantidad de reacciones necesarias para "+
														"destacar mensajes.")
		else:
			await client.send_message(message.channel, "La cantidad de reacciones necesarias para destacar un mensaje es "+
														"de: **"+minimo_destacados+"**.")
	elif len(mensaje_separado) > 3:
		await client.send_message(message.channel, "Para hacerte llamar profesional creo que necesitas demasiada "+
													"suerte. Sólo dime el número y nada más.")
	elif message.author.server_permissions.manage_channels or message.author.server_permissions.manage_messages:
		try:
			mensaje_separado[1] = int(mensaje_separado[1])
			if minimo_destacados == None:
				bd.execute("INSERT INTO destacados(minimo) VALUES(%s)", (mensaje_separado[1],))
			else:
				bd.execute("UPDATE destacados SET minimo = %s WHERE minimo = %s", (mensaje_separado[1], emoji_destacados))
			await client.send_message(message.channel, "**¡Ding ding ding!** La cantidad de reacciones necesarias para "+
														"destacar un mensaje es, ahora, de: **"+mensaje_separado[1]+"**.")
			base_de_datos.commit()
		except ValueError: await client.send_message(message.channel, "No necesitas suerte para saber que eso no "+
																		"es un número entero.")
	else:
		await client.send_message(message.channel, "Claro, ya lo hago**...\n...\n...\n...**\n"+
													"¡TE LA CREÍSTE! Sólo hago favores a los **profesionales**.")

async def crear_tabla(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	if whitelist[message.author.id] == "franco":
		BD_URL = os.getenv("DATABASE_URL")
		base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
		bd = base_de_datos.cursor()
		bd.execute(tabla_destacados)
		base_de_datos.commit()
		bd.close()
		base_de_datos.close()
		await client.send_message(message.channel, "Tarea finalizada.")
	else:
		await client.send_message(message.channel, "Buen intento pero sólo el profesional que me creó puede hacer eso.")