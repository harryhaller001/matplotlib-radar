# Minimal makefile for Sphinx documentation

.DEFAULT_GOAL := build-docs

# You can set these variables from the command line.
SPHINXOPTS    ?=
SPHINXBUILD   = python3 -m sphinx
SPHINXPROJ    = matplotlib_radar
SOURCEDIR     = source
BUILDDIR      = _build

help:
	@sphinx-build -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

build-docs: clean

# Generate example image
	python3 generate_example_plot.py

# Build html
	make html

.PHONY: help Makefile

clean:
	rm -rf "$(BUILDDIR)"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	sphinx-build -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
