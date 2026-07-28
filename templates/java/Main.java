import com.sun.net.httpserver.HttpServer;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) throws Exception {
        int porta = Integer.parseInt(System.getenv().getOrDefault("PORT", "3000"));

        // O '0.0.0.0' é obrigatório — sem ele o container sobe mas não responde de fora.
        HttpServer servidor = HttpServer.create(new InetSocketAddress("0.0.0.0", porta), 0);

        servidor.createContext("/", troca -> {
            byte[] corpo = "{\"status\":\"ok\"}".getBytes();
            troca.getResponseHeaders().add("content-type", "application/json");
            troca.sendResponseHeaders(200, corpo.length);
            try (OutputStream saida = troca.getResponseBody()) {
                saida.write(corpo);
            }
        });

        servidor.setExecutor(Executors.newFixedThreadPool(64));
        servidor.start();
        System.out.println("ouvindo na porta " + porta);
    }
}
