from typing import Mapping
import os
import webbrowser
import platform
import psutil
from flask import Flask, render_template, request

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def index():
    """
    Index function for render main application
    """
    context = {'RAM': '',
               'USERS': '',
               'CPU': '',
               'OS': ''
               }

    if request.method == 'POST':
        context['RAM'] = psutil.virtual_memory()
        context['USERS'] = psutil.users()
        context['CPU'] = psutil.cpu_stats()
        context['OS'] = f'{platform.system()} - {platform.version()}'

    return render_template('index.html', context=context)


if __name__ == '__main__':

    application.debug = False
    HOST = os.environ.get('IP', '127.0.0.1')
    PORT = int(os.environ.get('PORT', 5000))
    application.run(host=HOST, port=PORT)
