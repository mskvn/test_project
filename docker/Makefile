IMAGE_NAME=mskvn/test_project
IMAGE_VERSION=v0.2

.PHONY: docker_image build tag push

docker_image: build tag push

build:
	cp ../requirements.txt ./tmp/
	docker build  -t ${IMAGE_NAME}:${IMAGE_VERSION} .
tag:
	docker tag ${IMAGE_NAME}:${IMAGE_VERSION} ${IMAGE_NAME}:latest
push:
	docker push ${IMAGE_NAME}:${IMAGE_VERSION}
	docker push ${IMAGE_NAME}:latest
