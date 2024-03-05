SHELL=/bin/bash
.PHONY: build
.ONESHELL:
.EXPORT_ALL_VARIABLES:

VERSION=$(shell git describe --tags)
MESSAGE=$(shell git log -1 --pretty=format:%B)

version:
	git fetch --tags --all
	standard-version \
		--release-as minor \
		--skip.changelog \
		--skip.commit || exit 1

push-version:
	git push --follow-tags origin ${VERSION}

release:
	gh release create ${VERSION} --title "Release ${VERSION}" --notes "${MESSAGE}"

ci-release: version push-version release

dist:
	python setup.py sdist

pypi-test:
	twine upload --config-file .pypirc -r testpypi dist/kivera-sdk-*.tar.gz

pypi:
	twine upload --config-file .pypirc dist/kivera-sdk-*.tar.gz