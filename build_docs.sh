#!/bin/bash

# Navigate to the Sphinx documentation directory
cd docs

# Build the docs .rst files
sphinx-apidoc -o source/ ../

# Build the Sphinx documentation
make html

# Navigate back to the root directory
cd .. || exit
