python setup.py sdist bdist_wheel
twine upload dist/*
pip uninstall Nexgram.py -y
rm -rf build
rm -rf dist
rm -rf Nexgram.py.egg-info