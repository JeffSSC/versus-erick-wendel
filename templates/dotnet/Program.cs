var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => Results.Json(new { status = "ok" }));

var porta = Environment.GetEnvironmentVariable("PORT") ?? "3000";

// O '0.0.0.0' é obrigatório — sem ele o container sobe mas não responde de fora.
app.Run($"http://0.0.0.0:{porta}");
