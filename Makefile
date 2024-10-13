extract:
	pybabel extract bot -o locales/messages.pot

init:
	pybabel init -i locales/messages.pot -d locales -D messages -l en
	pybabel init -i locales/messages.pot -d locales -D messages -l uz
	pybabel init -i locales/messages.pot -d locales -D messages -l ru

update:
	pybabel update -d locales -D messages -i locales/messages.pot

compile:
	pybabel compile -d locales -D messages

