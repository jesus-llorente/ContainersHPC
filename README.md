# Chapter 1: Docker Roadmap

**Container vs environment**: 

A conda/venv environment isolates only the language-level package set; it still shares the host's OS, system libraries, and kernel. 

A container isolates the entire userspace (OS libraries, binaries, everything) via kernel namespaces.

Hence it's reproducible regardless of what's actually installed on the host machine: much stronger guarantee.

**Daemon**:

A background process that runs continuously and listens for requests, with no direct user interaction (started at boot, runs as a service). 

`dockerd` is Docker's daemon: it's the thing that actually builds and runs containers. 

The docker command you type is just a client that sends requests to that daemon over a socket; you never run containers "yourself," you ask the daemon to.

**Where the built image lives**: 

inside `dockerd`, which on Mac runs inside a lightweight Linux VM that Docker Desktop manages (macOS has no native kernel namespaces/cgroups, hence the VM). 

Layers get stored there, content-addressed, in that VM's internal storage — not as a file anywhere on your actual Mac filesystem. 

That's exactly why `ll /app` or looking for the image as a file earlier showed nothing: it only exists inside Docker's managed VM.

## Steps

1. Write `pipeline.py` (stdlib-only: reads `data/sample.csv`, prints JSON summary stats).

2. Write `Dockerfile` (`FROM python:3.11-slim`, `COPY`, `CMD`).

3. `docker build -t containers101-docker .` — build the first image, run it with `docker run --rm containers101-docker`.

4. Explore image vs container: `-it` for an interactive shell, `--rm` to avoid leftover stopped containers, `docker images` / `docker system df` to inspect and clean up old 
images.

5. Add `requirements.txt` (tensorflow) + `RUN pip install -r requirements.txt` in the Dockerfile, before `COPY`, for layer caching.

6. Learn architecture matters: Mac = arm64, Windows colleague = amd64 — a plain build only targets your own chip.

7. Build + share two ways: 
`docker buildx build --platform linux/arm64 --load` → `docker save` → `containers101-flow.tar` (for the Mac colleague, same arch); 
`--platform linux/amd64` → `containers101-flow-windows.tar` (for the Windows colleague).

8. Log in to Docker Hub (`docker login`) as an alternative distribution path (`push`/`pull` instead of tar files).
