import os
from flask import Flask

app=Flask(__name__)
	

			
class Command:
    def execute(self): pass

class Loony(Command):
    def execute(self):
        return("Command Pattern Says: HELLO!!")
# An object that holds commands:
class Macro:
    def __init__(self):
        self.commands = []
    def add(self, command):
        self.commands.append(command)   
    def run(self):
    	for c in self.commands:
    		c.execute()
    @app.route('/')
    def hello():
		macro = Macro()
		macro.add(Loony())
		macro.run()
		return macro.run()
   
    		       
	
	
if	__name__ =='__main__':	
	port=int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0', port=port)
	
	
	
	
	
