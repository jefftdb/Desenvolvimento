
from flask import Flask
import os 

app = Flask(__name__, template_folder=os.path.abspath('view/templates'), static_folder=os.path.abspath("view/static"))



from controller.video_nugget_controller import *





