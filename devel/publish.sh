rm -rf build/ dist/ isosplit5.egg-info/
python3 setup.py sdist
twine upload dist/*
