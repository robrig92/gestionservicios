import hashlib
import datetime
import time


class StringUtils():
	"""

			Clase de ayuda encargada del manejo
		de cadenas en el sistema.

		@author Paulo_Angeles.

	"""
	@staticmethod
	def randomHash():
		"""
			Sprint: 1

				Método encargado de generar random
			hash usando el tiempo como llave. 

				Este método hace uso del algoritmo de
			encriptamiento sha256.

			@author Paulo_Angeles.
		"""
		milis = int(round(time.time() * 1000))
		hash64 = hashlib.sha256(str(milis).encode('utf-8')).hexdigest()
		return hash64
