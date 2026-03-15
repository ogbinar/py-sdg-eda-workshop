FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.9.35/quarto-1.9.35-linux-amd64.deb \
    && dpkg -i quarto-1.9.35-linux-amd64.deb \
    && rm quarto-1.9.35-linux-amd64.deb

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /workspace
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

CMD ["bash"]
