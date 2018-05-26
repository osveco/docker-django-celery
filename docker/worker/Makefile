VERSION ?= $(shell date +%Y%m%d)
ORGANIZATION ?= $(shell id -un)
SUDO ?= "sudo"
NAME=$(shell basename `pwd`)

build:
	$(SUDO) mkdir myproject
	$(SUDO) mount --bind ../myproject ./myproject
	$(SUDO) docker build -t $(ORGANIZATION)/$(NAME):$(VERSION) .
	$(SUDO) docker tag $(ORGANIZATION)/$(NAME):$(VERSION) $(ORGANIZATION)/$(NAME):latest
	$(SUDO) umount ./myproject
	$(SUDO) rm -r myproject

push:
	$(SUDO) docker push $(ORGANIZATION)/$(NAME):$(VERSION)
	$(SUDO) docker push $(ORGANIZATION)/$(NAME):latest
