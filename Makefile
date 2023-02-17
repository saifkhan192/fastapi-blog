setup_local:
	python3 -m venv venv && python3 -m pip install -r functions/requirements.txt

setup_test_local:
	python3 -m venv venv && python3 -m pip install -r tests/requirements.txt

run_local:
	environment=dev uvicorn app.main:app --reload --port 8001

run_unit_tests_with_echo:
	python -m pytest tests/unit -v --capture=no

# run_integration_tests:
# 	python -m pytest tests/integration -v

# run_integration_tests_with_echo:
# 	python -m pytest tests/integration -v --capture=no

clear_cache:
	find . -type d -name __pycache__ -exec rm -r {} \+
	rm -rf .pytest_cache .aws-sam

test:
	PYTHONPATH=. pytest --capture=no
