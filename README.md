# Requirements

* docker
* python 3.6.8
* all packages from requirements.txt
* allure command line util for generate and open report (https://docs.qameta.io/allure/)


# Run tests

```shell
pytest -s --alluredir allure-results tests/
```

For not linux based systems:

```shell
pytest -s --start_app_in_docker --alluredir allure-results tests/
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

# Run all tests in docker container and generate allure report

```shell
./run_tests_in_docker.sh
```

You can find repost in `allure-report` folder.
For see report open `allure-report/index.html` in your favorite browser