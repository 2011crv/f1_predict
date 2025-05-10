FULL_IMAGE = 2011crv/f1:latest # TODO: change to org

.PHONY: build push rebuild run clean

build:
	@echo "🔧 Building Docker image: $(FULL_IMAGE)"
	@docker build -t $(FULL_IMAGE) .

push:
	@echo "🚀 Pushing Docker image to Docker Hub: $(FULL_IMAGE)"
	@docker push $(FULL_IMAGE)

rebuild:
	@echo "♻️ Rebuilding image from scratch (no cache)..."
	@docker build --no-cache -t $(FULL_IMAGE) .
	@echo "🚀 Pushing rebuilt image..."
	@docker push $(FULL_IMAGE)

run:
	@echo "🐳 Pulling latest image and launching interactive shell..."
	@docker pull $(FULL_IMAGE) > /dev/null
	@docker run -it $(FULL_IMAGE)

clean:
	@echo "🧹 Cleaning up local Docker image: $(FULL_IMAGE)"
	@docker rmi $(FULL_IMAGE) || true