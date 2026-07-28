# versus-erick-wendel

Erick Wendel sem teclado vs. 3 júniors — 2 horas pra fazer uma bilheteria aguentar
10 mil pessoas brigando por 100 ingressos.

## Começando (leva 1 minuto)

Copie o template da sua linguagem pra sua pasta e suba:

```bash
cp -r templates/node/. erick/        # node, python, go, java ou dotnet
docker compose up --build erick
```

Em outro terminal, confirme que respondeu:

```bash
curl http://localhost:7811/
```

Voltou `{"status":"ok"}`? Está de pé. Agora é só implementar o contrato por cima.

## Pastas

| Pasta      | Quem                        | Porta no seu navegador |
| ---------- | --------------------------- | ---------------------- |
| `erick/`   | Erick                       | 7811                   |
| `juniors/` | os 3 júniors, um projeto só | 7812                   |

Dentro da sua pasta, organize como quiser. O único arquivo obrigatório é o
`Dockerfile` na raiz:

```
erick/
├── Dockerfile      ← obrigatório, na raiz
├── index.js
└── (o resto do seu jeito: src/, models/, o que for)
```

## Comandos

```bash
docker compose up --build erick      # sobe (rebuilda se mudou o código)
docker compose up --build juniors    # sobe o outro time

docker compose logs -f erick         # ver os logs
docker compose restart erick         # reiniciar sem rebuildar
docker compose down                  # derruba tudo
```

Rode **um sistema por vez** na hora do teste, pra não disputarem CPU.

Mudou o código? `Ctrl+C` e `docker compose up --build erick` de novo.

## Regras

São 3, e estão no **[CONTRIBUTING.md](./CONTRIBUTING.md)**:

1. A API escuta na porta **3000** (dentro do container)
2. Escutando em **`0.0.0.0`**, nunca em `127.0.0.1`
3. Um **`Dockerfile`** na raiz da sua pasta

A linguagem é livre. Os templates em [`templates/`](./templates/) já vêm com tudo isso
pronto e testado.

---

## Antes da gravação (Gabriel)

Com ambiente offline, o build não baixa nada. Puxe as imagens base antes:

```bash
docker pull node:22-alpine
docker pull python:3.13-slim
docker pull golang:1.24-alpine
docker pull eclipse-temurin:21-jdk
docker pull mcr.microsoft.com/dotnet/sdk:9.0
```

Se alguém for usar framework (Express, FastAPI, Spring), aí precisa de internet no
momento do build — ou libera a rede, ou o `node_modules`/pacotes vão junto no PR.
