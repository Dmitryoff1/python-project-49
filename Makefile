install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games
brain-even:
	poetry run brain-even
brain-cals:
	poetry run brain-cals
brain-gcd:
	poetry run brain-gcd
