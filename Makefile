FILES := $(wildcard *.v)
NAMES := $(FILES:%.v=%) # $(patsubst %.v,%,$(FILES))
V = $(shell which v)


all: $(NAMES)

$(NAMES):
	@echo "- $@ -"
	@$(V) run $@.v
