target_dir = "kjr_llm/"

run_ruff:
	ruff check --fix $(target_dir)

run_mypy:
	mypy $(target_dir) --ignore-missing-imports --follow-imports=skip

run_all: run_ruff run_mypy
	@echo "All checks run"
