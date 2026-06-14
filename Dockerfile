# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for tafsiri-mcp
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/tafsiri-mcp"
LABEL org.opencontainers.image.description="tafsiri-mcp — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir tafsiri-mcp

CMD ["tafsiri-mcp"]
