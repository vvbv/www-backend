import requests
import json
class ApiPagos:
    URL_BASE = 'https://www-pagos-luchoman.c9users.io'
    URL_CAJERO_ONLINE = URL_BASE + '/cajero_online/'
    URL_VALIDAR_TARJETA = URL_CAJERO_ONLINE + 'validar-numero-cuenta/'
    URL_TRANSFERENCIA = URL_CAJERO_ONLINE + '/transferir/'
    CODIGO_TARJETA_VALIDA = 8
    
    def url_transferencia(self, key, id_cuenta_origen, id_cuenta_destino, valor_transaccion, password):
        return self.URL_TRANSFERENCIA + str(key) + '/' + str(id_cuenta_origen) + '/' +  str(id_cuenta_destino )+ '/' + str(valor_transaccion) + '/' + str(password) + '/'
        
    def url_validar_tarjeta(self, numero_tarjeta, password):
        return self.URL_VALIDAR_TARJETA + str(numero_tarjeta) + '/' + str(password) + '/'
        
    def transaccion(self, key, id_cuenta_origen, id_cuenta_destino, valor_transaccion, password ):
        url = self.url_transferencia(key, id_cuenta_origen, id_cuenta_destino, valor_transaccion, password)
        respuestaJSON = json.loads(requests.get(url))
        return respuestaJSON
        
    def validar_tarjeta(self, numero_tarjeta, password):
        url = self.url_validar_tarjeta(numero_tarjeta, password)
        print (url)
        respuestaJSON = requests.get(url).json()
        if int(respuestaJSON['codigo']) == self.CODIGO_TARJETA_VALIDA:
            return True, respuestaJSON['mensaje']
        else:
            return False, respuestaJSON['mensaje']
        
        