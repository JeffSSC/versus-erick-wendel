FROM mcr.microsoft.com/dotnet/sdk:9.0

WORKDIR /app
COPY . .

RUN dotnet publish -c Release -o out

ENV PORT=3000
EXPOSE 3000

# Pega o dll publicado, qualquer que seja o nome do projeto.
CMD ["sh", "-c", "dotnet out/*.dll"]
