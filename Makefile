
# If the first argument is "app"...
ifeq (app,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "app"
  APP_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(APP_ARGS):;@:)

ifeq ($(APP_ARGS), $(" "))
	APP_ARGS := newapp
endif
endif


.PHONY: help
help:
	@echo
	@echo "  make venv         Create and inizialize a venv in, well, ./venv"
	@echo "                    Addiitonally, will clone my remi repo to ../remi if missing"
	@echo "  make app <name>   Create a copy of template.py and name it <name>.py"
	@echo


.PHONY: venv
venv:
	@bash -c "if [ ! -d ../remi ]; then echo 'Please clone remi in ../remi'; else rm -rf venv && python -m venv venv && source venv/bin/activate && pip install -e ../remi  && pip install -r requirements.txt ; fi"

.PHONY: app
app:
#ifeq ($(APP_ARGS), newapp)
#	@echo "Creating newapp, you could name it with `make app myapp`"
#endif
	@bash -c '[ "$(APP_ARGS)" == "newapp" ] && echo "Creating newapp, you could name it with \"make app myapp\"" || echo "Creating $(APP_ARGS).py" ; cp spinner.py $(APP_ARGS).py'
