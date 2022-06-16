install-test:
	pip install -q -r requirements/test.txt

install-dev:
	pip install -q -r requirements/dev.txt

install: install-test

quality:  ## Run the quality checks
	pycodestyle --config=.pep8 done
	pylint --rcfile=pylintrc done
	python setup.py -q sdist
	twine check dist/*

test:  ## Run the tests
	mkdir -p var
	rm -rf .coverage
	python -m coverage run --rcfile=.coveragerc ./test.py --noinput

covreport:  ## Show the coverage results
	python -m coverage report -m --skip-covered

COMMON_CONSTRAINTS_TXT=requirements/common_constraints.txt
.PHONY: $(COMMON_CONSTRAINTS_TXT)
$(COMMON_CONSTRAINTS_TXT):
	wget -O "$(@)" https://raw.githubusercontent.com/edx/edx-lint/master/edx_lint/files/common_constraints.txt || touch "$(@)"

upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: $(COMMON_CONSTRAINTS_TXT)  ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	pip install -q -r requirements/pip_tools.txt
	pip-compile --upgrade -o requirements/pip_tools.txt requirements/pip_tools.in
	pip-compile --upgrade -o requirements/base.txt requirements/base.in
