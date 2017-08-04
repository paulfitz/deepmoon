sdist:
	rm -rf dist
	cp README.md README
	python setup.py sdist
	ls -l dist/deepmoon*.tar.gz
	sleep 5
	cd dist && mkdir tmp && cd tmp && tar xzvf ../deepmoon*.tar.gz && cd deepmoon*[0-9] && ./setup.py build
	python setup.py sdist upload
	rm -rf dist
	rm README
