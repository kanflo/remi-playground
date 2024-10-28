venv:
	@bash -c "if [ ! -d ../remi ]; then echo 'Please clone remi in ../remi'; else rm -rf venv && python -m venv venv && source venv/bin/activate && pip install -e ../remi ; fi"
