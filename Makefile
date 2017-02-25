SHELL=/bin/sh

init:
	@echo 'pip install -r requirements.txt'

test:
	@echo 'test'

.PHONY: init test
