
all: tests run

run:
	python bulls.py

tests:
	python -mdoctest bulls.py
