#!/usr/bin/env python3
# coding: utf-8

import re
import requests
from mcstatus import JavaServer
from flask import Flask, render_template, render_template_string, request


FLAG = requests.get('http://mc-players-flag:1337/').text

app = Flask(__name__, template_folder='./')
app.config['DEBUG'] = False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method != 'POST' or 'server' not in request.form.keys():
        return render_template('index.html')

    server = request.form['server'].split(':')
    if len(server) == 2:
        hostname = server[0]
        port = int(server[1])
    else:
        hostname = server[0]
        port = 25565

    try:
        ms = JavaServer(hostname, port)
        status = ms.status()
    except:
        error = '''
            <br>
            <div class='alert alert-danger' role='alert'>
                An error occurred while communicating with the MC server.
            </div>
        '''
        return render_template('index.html', error=error)

    players = []
    if status.players.sample is not None:
        for player in status.players.sample:
            if re.match(r'\w*', player.name) and len(player.name) <= 20:
                players.append(player.name)

    html_player_list = f'''
        <br>
        <h3>{hostname} ({len(players)}/{status.players.max})</h3>
        <ul>
    '''
    for player in players:
        html_player_list += '<li>' + player + '</li>'
    html_player_list += '</ul>'

    results = render_template_string(html_player_list)
    return render_template('index.html', results=results)


@app.route('/flag', methods=['GET'])
def flag():
    if request.remote_addr != '13.37.13.37':
        return 'Unauthorized IP address: ' + request.remote_addr
    return FLAG


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2156, threaded=False)
