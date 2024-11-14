.DEFAULT_GOAL := build-docs

SPHINXOPTS    ?=
SOURCEDIR     = source
BUILDDIR      = build

help:
	@sphinx-build -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

build-docs:

# Generate example image
	python3 generate_example_plot.py

# Remove pre build
	rm -rf build

# Build html
	make html

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	sphinx-build -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
