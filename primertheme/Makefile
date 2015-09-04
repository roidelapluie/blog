extract:
	pybabel extract -F babel.cfg -o messages.pot --copyright-holder="Julien Pivotto <roidelapluie@inuits.eu>" --msgid-bugs-address=roidelapluie@inuits.eu  --project=roidelapluie.be .
	pybabel update -l fr -d ./translations/ -i ./messages.pot
	pybabel compile -f -d ./translations/

