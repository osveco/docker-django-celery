VERSION ?= $(shell date +%Y%m%d)
ORGANIZATION ?= "datacap"
SUDO ?= "sudo"

build: \
	docker-web \
	docker-worker
     

compose-%:
	$(eval CMD := $(patsubst compose-%,%,$@))
	(cd docker && docker-compose $(CMD))

docker-%:
	$(eval IMAGE := $(patsubst docker-%,%,$@))
	@echo "== Building image $(ORGANIZATION)/$(IMAGE)"
	(cd docker/$(IMAGE) && make ORGANIZATION=$(ORGANIZATION) VERSION=$(VERSION) SUDO=$(SUDO))

