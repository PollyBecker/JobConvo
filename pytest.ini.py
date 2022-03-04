import that as that

[pytest]
DJANGO_SETTINGS_MODULE = test.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py= test.settings
addopts=
    --doctest-modules
    --strict-markers
markers=
    slow= run tests that are slow
    fast= run tests that are fast