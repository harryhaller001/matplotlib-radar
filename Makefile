
# Declare global variables

BASE_DIR			= ${PWD}

PACKAGE_NAME		= matplotlib-radar

PACKAGE_DIR			= $(BASE_DIR)/matplotlib_radar
TEST_DIR			= $(BASE_DIR)/tests
DOCS_DIR			= $(BASE_DIR)/docs

UV_OPT				= uv
UV_RUN_OPT			= uv run
TY_OPT				= $(UV_RUN_OPT) ty
TEST_OPT			= $(UV_RUN_OPT) pytest
TWINE_OPT			= $(UV_RUN_OPT) twine
SPHINX_OPT			= $(UV_RUN_OPT) python -m sphinx
COVERAGE_OPT		= $(UV_RUN_OPT) coverage
FLIT_OPT			= $(UV_RUN_OPT) flit
RUFF_OPT			= $(UV_RUN_OPT) ruff
PRE_COMMIT_OPT		= $(UV_RUN_OPT) pre-commit

# Run help by default

.DEFAULT_GOAL := help



.PHONY : help
help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)




# Dependency handling

.PHONY : install
install: ## install all python dependencies

# Install dev dependencies
	$(UV_OPT) sync --all-extras

# Install pre-commit hooks
	@$(PRE_COMMIT_OPT) install



.PHONY : build
build: ## Twine package upload and checks

	@rm -rf ./dist/*

	$(UV_OPT) build

# Check package using twine
	@$(TWINE_OPT) check --strict ./dist/*


.PHONY : format
format: ## Lint and format code with flake8 and black
	@$(RUFF_OPT) format $(PACKAGE_DIR) $(TEST_DIR) $(DOCS_DIR)/source/conf.py
	@$(RUFF_OPT) check --fix $(PACKAGE_DIR) $(TEST_DIR) $(DOCS_DIR)/source/conf.py


.PHONY: testing
testing: ## Unittest of package
	@$(COVERAGE_OPT) run -m pytest
	@$(COVERAGE_OPT) html

# Long coverage report
	@$(COVERAGE_OPT) report -m


.PHONY: typing
typing: ## Run static code analysis
	@$(TY_OPT) check $(PACKAGE_DIR) $(TEST_DIR) $(DOCS_DIR)/source/conf.py




.PHONY: docs
docs: ## Build sphinx docs
	@rm -rf ./docs/_build

	@$(SPHINX_OPT) -M doctest $(DOCS_DIR)/source $(DOCS_DIR)/_build
	@$(SPHINX_OPT) -M coverage $(DOCS_DIR)/source $(DOCS_DIR)/_build

# Build HTML version
	@$(SPHINX_OPT) -M html $(DOCS_DIR)/source $(DOCS_DIR)/_build



.PHONY: check ## Full check of package
check: install format typing testing docs precommit build



.PHONY : precommit
precommit: ## Run precommit file
	@$(PRE_COMMIT_OPT) run --all-files
