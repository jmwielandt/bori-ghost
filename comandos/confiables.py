import os
import discord
import psycopg2
from funciones import get_confiables, get_confiable_role
from variables import nuevo_confiable, quita_confiable

async def confiables(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	if message.author.server_permissions.manage_roles:
		BD_URL = os.getenv("DATABASE_URL")
		base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
		bd = base_de_datos.cursor()
		confiables = get_confiables()
		for miembro in message.mentions:
			confiable_rol = get_confiable_role(miembro.server.roles)
			if miembro.id in confiables:
				bd.execute(quita_confiable, (miembro.id,))
				await client.remove_roles(miembro, confiable_rol)
				await client.send_message(message.channel, "Ahora {} ya no es un usuario confiable.".format(miembro.display_name))
			else:
				bd.execute(nuevo_confiable, (miembro.id,))
				await client.add_roles(miembro, confiable_rol)
				await client.send_message(message.channel, "Ahora {} es un usuario confiable.".format(miembro.display_name))
		else:
			error_faltan = "Chico, déjame seguir con mi jueguito de Star Wars, tienes que mencionar usuarios para hacer eso, {}."
			await client.send_message(message.channel, error_faltan.format(message.author.display_name))
		bd.close()
		base_de_datos.commit()
		base_de_datos.close()
	else:
		error = "Espérame un momentito... Sí, eso es. Como pensaba, no eres lo suficientemente profesional como para hacer eso"+\
		"mejor cómprate una MAC, {}."
		await client.send_message(message.channel, error.format(message.author.display_name))