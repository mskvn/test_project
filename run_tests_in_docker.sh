cmd="pip install -r requirements.txt && pytest -s --alluredir allure-results tests/; allure generate allure-results -o allure-report -c"
echo $cmd

docker run  \
  -v "$(pwd):/root/" \
  -w "/root/" \
  mskvn/test_project:v0.2 \
  /bin/bash -c "$cmd"
