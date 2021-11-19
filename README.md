# grafana-render-slack

Get grafana rendered images and post on a slack channel. 

## Usage 

```
usage: ./grafana-render-get.py --url "[URL RENDERED IMG]" --apikey "[GRAFANA API TOKEN]" --slacktoken "[SLACK TOKEN]" --slackchannel "[SLACK CHANNEL]" --slacktitle "[TITLE]"

Grafana Render Get generate a rendered image of a panel.

optional arguments:
  -h, --help            show this help message and exit
  --url URL             Dashboard url.
  --apikey APIKEY       Api Key.
  --slacktoken SLACKTOKEN
                        Api Token for Slack notification.
  --slackchannel SLACKCHANNEL
                        Slack #Channel.
  --slacktitle SLACKTITLE
                        Slack title of the image.
  --version             show program's version number and exit

```
