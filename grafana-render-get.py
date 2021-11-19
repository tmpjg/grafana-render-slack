#!/usr/bin/env python3

import sys
import requests
import tempfile
import argparse

""" Parse """

parser = argparse.ArgumentParser(description='Grafana Render Get generate a rendered image of a panel.' , usage='./grafana-render-get.py --url "[URL RENDERED IMG]" \
--apikey "[GRAFANA API TOKEN]" --slacktoken "[SLACK TOKEN]" --slackchannel "[SLACK CHANNEL]" --slacktitle "[TITLE]"')
parser.add_argument('--url', help='Dashboard url.',type=str,required=True)
parser.add_argument('--apikey', help='Api Key.',type=str,required=True)
parser.add_argument('--slacktoken', required=True, type=str, help='Api Token for Slack notification.')
parser.add_argument('--slackchannel', required=True, type=str, help='Slack #Channel.')
parser.add_argument('--slacktitle', required=True, type=str, help='Slack title of the image.')
parser.add_argument('--version', action='version', version='1.0.0')
args = parser.parse_args()


""" src """ 

def grafanaget(url,apikey):	
    try: 
        headers = {'Authorization' : 'Bearer %s' % (apikey)} 
        r = requests.get(url,headers=headers,stream=True) 
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            # Open a local file with wb ( write binary ) permission.
            filename = tempfile.NamedTemporaryFile(prefix="grafana_render_", suffix=".png")
            open(filename.name, 'wb').write(r.content)
            return filename
        else:
            raise Exception('Image Couldn\'t be retreived') 
    except Exception as e:
        raise Exception(e) 

def slackpost(filename, token, channel, title):
    try:
        f = {'file': (filename, open(filename, 'rb'), 'image/png', {'Expires':'0'})}
        r = requests.post(url='https://slack.com/api/files.upload', \
                data={'token': token, 'channels': channel, 'media': f, 'title': title},headers={'Accept': 'application/json'}, files=f)
        if '"ok":false' in r.text:
            raise Exception(r.text)
    except Exception as e: 
        raise e


def main(args):
    try:
        url = args.url
        apikey = args.apikey
        slacktoken = args.slacktoken
        slackchannel = args.slackchannel
        slacktitle = args.slacktitle
        img = grafanaget(url,apikey)
        slackpost(img.name,slacktoken,slackchannel,slacktitle)
    except Exception as e: 
        print(e)




if __name__ == '__main__':
    sys.exit(main(args))

