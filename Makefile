.PHONY: help
help:
	@echo "Commands:"
	@echo "venv               : sets up virtual environment for development."
	@echo "api                : launches FastAPI app."
	@echo "streamlit          : runs streamlit app."

# Set up virtual environment
.PHONY: venv
venv:
	python3 -m venv venv && \
	. venv/bin/activate && \
	python3 -m pip install --upgrade pip setuptools wheel && \
	python3 -m pip install -r requirements.txt


# python3 scripts/download_checkpoint.py kingyiusuen/image-to-latex/1w1abmg1

# API
.PHONY: api
api:
	. venv/bin/activate
	python3 -m uvicorn api.app:app --host 10.129.0.12 --port 8001 --reload --reload-dir image-to-latex --reload-dir api

# Streamlit
.PHONY: streamlit
streamlit:
	. venv/bin/activate
	streamlit run streamlit/app.py
