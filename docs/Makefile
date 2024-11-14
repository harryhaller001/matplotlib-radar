.DEFAULT_GOAL := help

SPHINXOPTS    ?=
SOURCEDIR     = source
BUILDDIR      = build

help:
	@sphinx-build -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

build-docs:
	cp ../README.md ./source/introduction.md
	rm -rf build
	make html

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	sphinx-build -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
