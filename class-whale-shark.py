class whaleshark:
	def __init__(self, body, fins, eyes, fur, reptile):
		self.fins = fins
		self.body = body
		self.eyes = eyes
		self.fur = fur
		self.reptile = reptile

	def describe(self):
		print("description")
		print(f"finspan: {self.fins}")
		print(f"bodylength: {self.body}")
		print(f"eyecount: {self.eyes}")
		print(f"furry?: {self.fur}")
		print(f"reptile?: {self.reptile}")

whaleshark = whaleshark(13.5, 18.3, 2, False, False)
whaleshark.describe()