import phonenumbers
from phonenumbers import geocoder, carrier

# Digite seu número com codigo do país e ddd #
phoneNumer = phonenumbers.parse("+5551999999999")

# Captura operadora #
Carrier = carrier.name_for_number(phoneNumer, 'pt-br')

# Captura região #
Region = geocoder.description_for_number(phoneNumer, 'pt-br')

# Mostra resultados #
print("A operadora é: " + Carrier)
print("O estado é: " + Region)