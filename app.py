import init
def createApp(envivorment=None, start_response=None):
    with init.app.app_context():
        init.create_app()
    return init.app
