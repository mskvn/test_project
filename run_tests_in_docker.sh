cmd="pip install -r requirements.txt && pytest -s --alluredir allure-results tests/"
echo $cmd

docker run  \
  -v "$(pwd):/root/" \
  -w "/root/" \
  mskvn/test_project:v0.1 \
  /bin/bash -c "$cmd"
