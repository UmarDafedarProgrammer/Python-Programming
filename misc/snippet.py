import os
import pyvis

pyvis_dir = os.path.dirname(pyvis.__file__)
templates_dir = os.path.join(pyvis_dir, 'templates')
template_file = os.path.join(templates_dir, 'network.html')

print("Pyvis directory:", pyvis_dir)
print("Templates directory exists?", os.path.isdir(templates_dir))
print("network.html exists?", os.path.isfile(template_file))

