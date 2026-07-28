FROM eclipse-temurin:21-jdk

WORKDIR /app
COPY . .

# Java puro, sem Maven/Gradle — build instantâneo e funciona offline.
# Se você preferir Spring Boot, troque este bloco pelo build da sua ferramenta.
RUN javac Main.java

ENV PORT=3000
EXPOSE 3000

CMD ["java", "Main"]
