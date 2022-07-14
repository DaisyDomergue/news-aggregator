install-dependecies:
	pip install fastapi
	pip install pandas
	sudo apt install uvicorn

start:
	uvicorn index:app --reload

test:
	python -m unittest test.Testing
	