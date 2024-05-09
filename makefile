# Set the virtual environment directory
VENV_DIR = .venv

# Install dependencies
install:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

# Activate the virtual environment
activate:
	. $(VENV_DIR)/bin/activate

# Run tests
test:
	$(VENV_DIR)/bin/pytest tests/

# Run the application in debug mode
run:
	flask run --debugger --reload

# Freeze dependencies
freeze:
	$(VENV_DIR)/bin/pip freeze > requirements.txt

# Clean up
clean:
	rm -rf $(VENV_DIR)
