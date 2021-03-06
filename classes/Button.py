from utils import filter

class Button:

	text = ""
	onclick = ""
	href = ""

	def __init__(self, text, onclick="", href=""):
		self.text = filter.filter(text)
		self.onclick = onclick
		self.href = href

	def reparse(self):
		self.text = filter.filter(self.text)

	def getRaw(self):
		if self.href == "":
			return "<button onclick='" + self.onclick + "'>" + self.text + "</button>"
		else:
			return "<a href='" + self.href + "'><button onclick='" + self.onclick + "'>" + self.text + "</button></a>"
