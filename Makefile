run:
	@python data_preparation_project_package_folder/main.py

run_uvicorn:
	@uvicorn data_preparation_project_package_folder.api:app --reload

install:
	@pip install -e .

test:
	@pytest -v tests
