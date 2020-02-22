# Serienampel
Do you have the problem of having watched every series you know of, having virtually no real friends you can complain to about the horrendously bad recommendations Netflix gives you, because you watched **ONE** anime series or are you triggered by unclear financing of review sites and/or mentally impaired in any other way?

Well you have come to the right place, because this project is gonna protect you shitty existence from any outside influences that seek to destroy it. Get you recommendations on which series to waste your time on [serienampel.de](https://serienampel.de) and contribute to this project to make procrastination more socially acceptable,

# Usage
## Flask-Inbuilt

    usage: init.py [-h] [-i INTERFACE] [-p PORT] [-s SERVERNAME]
    
    serienampel server
    
    optional arguments:
      -h, --help            show this help message and exit
      -i INTERFACE, --interface INTERFACE
                            Interface to listen on (default: 0.0.0.0)
      -p PORT, --port PORT  Port to listen on (default: 5000)
      -s SERVERNAME, --servername SERVERNAME
                            External hostname (i.e. serienampel.de) (default:
                            None)

## WSGI (waitress)
Configuration can be done via *config.py*, port and interface must be specified in the command line or appropritate WSGI-runner configuration:

    apt install python3-waitress
    waitress-serve --host 127.0.0.1 --port 5000 --call 'app:createApp'

# Pictures
![Main Page](https://media.atlantishq.de/serienampel.png)    
