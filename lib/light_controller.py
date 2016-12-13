from websocket import create_connection


class LightController:
    def __init__(self, ws_url):
        self.ws_url = ws_url

    def power_on(self):
        self.__send_message('power_on')

    def power_off(self):
        self.__send_message('power_off')

    def __send_message(self, message):
        con = self.__create_connection()
        con.send(message)
        con.close()

    def __create_connection(self):
        return create_connection(self.ws_url)
