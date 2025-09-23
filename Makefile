start:
	uv run manage.py runserver 0.0.0.0:8000

fix_lint:
	uv run ruff check --fix .

install:
	uv sync

.PHONY: install