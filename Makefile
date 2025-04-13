.PHONY: test test-cov clean

test:
	pytest tests/

test-cov:
	pytest --cov=modular --cov-report=html tests/
	@echo "Coverage report is in htmlcov/index.html"

clean:
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 