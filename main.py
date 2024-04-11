from kivymd.app import MDApp
from kivy.lang import Builder

kv = """

MDAnchorLayout: 
	MDFloatingActionButton: 
		icon:"language-python"

"""

class App(MDApp): 
	def build(self): 
		return Builder.load_string(kv)
		
App().run()