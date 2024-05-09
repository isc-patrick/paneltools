__version__ = "0.1.0"

# Load the template   
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('templates/golden/'))
jinja_template = env.get_template('golden.html')
  