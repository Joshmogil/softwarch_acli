# The directory where you want your virtual environment.
VENV_DIR := venv
UVICORN := $(VENV_DIR)/bin/uvicorn
APP_MODULE := main:app

# The Python command you want to use. Change if necessary.
PYTHON := python3

.PHONY: setup
setup: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate:
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r requirements.txt

.PHONY: activate
activate:
	@echo "To activate the virtual environment, run: 'source $(VENV_DIR)/bin/activate'"

.PHONY: clean
clean:
	rm -rf $(VENV_DIR)

.PHONY: run-server
run-server:
	$(UVICORN) $(APP_MODULE) --reload