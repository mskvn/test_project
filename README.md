# Requirements

* docker
* python 3.6.8
* all packages from requirements.txt
* allure command line util for generate and open report (https://docs.qameta.io/allure/)


# Run tests

```shell
pytest -s --alluredir allure-results tests/
```

# Generate and open report

```shell
allure generate allure-results -o allure-report -c
allure open allure-report
```

or
```shell
allure serve allure-results
```
