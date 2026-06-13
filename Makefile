.PHONY: verify test sha clean

verify:
	bash RUN_ALL.sh

test:
	pytest -q

sha:
	python scripts/generate_sha256.py

clean:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
