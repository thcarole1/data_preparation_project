from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="data_preparation_project",
      description="pPresent the main techniques to prepare data for a machine learning project",
      packages=find_packages(), # NEW: find packages automatically
     install_requires=requirements) # NEW
