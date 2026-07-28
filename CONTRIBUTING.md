# Como entregar

Você vai abrir um Pull Request com **uma pasta só sua**. Tudo que importa está em três regras.

O que a API precisa fazer está no **contrato impresso, em cima da mesa**. Este arquivo
aqui é só sobre como empacotar e entregar.

## As 3 regras

### 1. Sua API escuta na porta 3000

Dentro do container, sempre a porta 3000. Não precisa se preocupar com conflito: cada
sistema roda isolado, e o mapeamento pra máquina de teste é feito automaticamente.

### 2. Escute em `0.0.0.0`, nunca em `127.0.0.1`

**Este é o erro que mais derruba gente.** Se a sua API escutar em `localhost`, ela sobe
sem erro nenhum e o teste não consegue falar com ela — parece que o sistema está de pé,
mas nada responde.

| Linguagem | Certo |
|---|---|
| Node/Express | `app.listen(3000, '0.0.0.0')` |
| Python/FastAPI | `uvicorn.run(app, host="0.0.0.0", port=3000)` |
| Go | `http.ListenAndServe("0.0.0.0:3000", nil)` |
| Java/Spring | `server.address=0.0.0.0` e `server.port=3000` |
| .NET | `app.Urls.Add("http://0.0.0.0:3000")` |

### 3. Tenha um `Dockerfile` na raiz da sua pasta

Não escreva do zero — copie o projeto pronto da sua linguagem em
[`templates/`](./templates/), que já sobe respondendo HTTP:

```bash
cp -r templates/node/. erick/
```

## Onde colocar seu código

```
erick/      → Erick
juniors/    → os 3 júniors, um projeto só
```

Dentro da sua pasta, organize os arquivos como quiser (`src/`, `models/`, o que preferir).
O `Dockerfile` é o único que precisa estar na raiz.

## Antes de abrir o PR: teste em 30 segundos

Rode isso na raiz do repositório, trocando `erick` pelo nome da sua pasta:

```bash
docker compose up --build erick
```

Em outro terminal:

```bash
curl http://localhost:7811/
```

Respondeu? Está entregue. Não respondeu? Quase sempre é a regra 2 (`0.0.0.0`).

> As portas externas: `erick` → `7811`, `juniors` → `7812`.

## Não esqueça do `POST /batch/reset`

É o endpoint mais fácil do contrato e o mais fácil de esquecer. Ele é chamado **antes de
cada rodada de teste** pra devolver o lote ao estado inicial.

Se ele não funcionar, sua rodada seguinte começa com o lote já esgotado — e o placar vai
mostrar isso na tela, ao vivo.

## Banco de dados

Se for usar banco, a sugestão é **SQLite** — roda dentro do seu próprio container, sem
precisar de serviço nenhum a mais.
