
.PHONY: deploy
deploy:
	@docker image rm -f bien-py-bot;\
docker build -t bien-py-bot .;\
docker rm -f bien-py-bot;\
docker run -d --restart unless-stopped --name bien-py-bot --env-file config.env bien-py-bot;\

.PHONY: start
start:
	@docker run -d --restart unless-stopped --name bien-py-bot --env-file config.env bien-py-bot