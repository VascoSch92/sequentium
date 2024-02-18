# Minimal makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help docs

clean:
	@echo "[Makefile] -- cleaning"
	@rm -rf "./$(BUILDDIR)"
	@rm -rf "./$(SOURCEDIR)/command-line-interface.md"
	@rm -rf "./$(SOURCEDIR)/contributing.md"
	@rm -rf "./$(SOURCEDIR)/quickstart.md"
	@rm -rf "./$(SOURCEDIR)/sequences-list.md"
	@rm -rf "./$(SOURCEDIR)/usage.md"
	@rm -rf "./$(SOURCEDIR)/changelog.md"

copy-pages:
	@echo "[Makefile] copying pages..."
	@cp -r ../docs/pages/usage.md "$(SOURCEDIR)/usage.md"
	@cp -r ../docs/pages/quickstart.md "$(SOURCEDIR)/quickstart.md"
	@cp -r ../docs/pages/how-to-contribute.md "$(SOURCEDIR)/contributing.md"
	@cp -r ../docs/pages/command‐line-interface.md "$(SOURCEDIR)/command‐line-interface.md"

copy-sequences-list:
	@echo "[Makefile] copying sequences list..."
	@cp -r ../sequence/SEQUENCES_LIST.md "$(SOURCEDIR)/sequences-list.md"

copy-changelog:
	@echo "[Makefile] copying changelog..."
	@cp -r ../CHANGELOG.md "$(SOURCEDIR)/changelog.md"

build-docs:
	@echo "[Makefile] -- build the documentation"
	@$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)"

generate-docs: clean copy-pages copy-sequences-list copy-changelog build-docs
