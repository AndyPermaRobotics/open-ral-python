# open-ral-python

This package contains reusable components to work with openRAL in python projects. 

For more informations about openRAL see: https://open-ral.io/


## Build package

Create a source distribution package with:
```bash
python setup.py sdist
```

### Install package from local source distribution

```bash
pip install ./dist/open_ral_python-{current-version}.tar.gz
```

### Publish package to PyPI (https://pypi.org/)

```bash
twine upload ./dist/*
```

### Publish package to TestPyPI (https://test.pypi.org/)

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

### Install package from TestPyPI

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ openral-py  
```

`--extra-index-url https://pypi.org/simple/` is needed for dependencies that are not available on PyPI.