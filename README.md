# Number Theory Toolkit

A toolkit of various algorithms used in number theory in pure Python. All algorithms are standalone and can be used out-of-the-box.

A full list of all the available algorithms includes:

* Prime Checking
* Sieve of Eratosthenes
* Binomial Coefficient
* Binomial Theorem
* Pascal's Triangle
* Euclidean Algorithm
* Bezout Coefficients
* Linear Congruence Solver
* Linear Congruence System Solver
* Chinese Remainder Theorem
* Public Key Encryption
* Public Key Decryption

## Installation

Clone the repository.

```bash
git clone https://github.com/f4str/number-theory-toolkit
```

Change directories into the cloned repository.

```bash
cd number-theory-toolkit
```

Install Python and create a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dev dependencies using pip.

```bash
pip install -e .[dev]
```

## Usage

All algorithms can be used by importing the corresponding function directly from the `number_theory_toolkit` package.

```python
from number_theory_toolkit import is_prime, linear_congruence

print(is_prime(123))
print(linear_congruence(2, 1, 5))
```

Each function has its different parameters. Refer to the individual function for more information on the expected inputs and outputs.

## Development

The `tox` library is used to run all tests and code formatting. This is automatically installed with the dev requirements. The available options are as follows.

* Run linting checks using `flake8`.

    ```bash
    tox -e lint
    ```

* Run type checks using `mypy`.

    ```bash
    tox -e type
    ```

* Run unit tests `pytest`.

    ```bash
    tox -e test
    ```

* Run all three of the tests above.

    ```bash
    tox
    ```

* Format the code using `black` and `isort` to comply with linting conventions.

    ```bash
    tox -e format
    ```

Upon pull request, merge, or push to the `master` branch, the three tests with `tox` will be run using GitHub Actions. The workflow will fail if any of the tests fail. See `.github/workflows/python-package.yml` for more information on how the CI works.
