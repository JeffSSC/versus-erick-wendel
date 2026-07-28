package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
)

func main() {
	porta := os.Getenv("PORT")
	if porta == "" {
		porta = "3000"
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("content-type", "application/json")
		json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
	})

	// O '0.0.0.0' é obrigatório — sem ele o container sobe mas não responde de fora.
	log.Printf("ouvindo na porta %s", porta)
	log.Fatal(http.ListenAndServe("0.0.0.0:"+porta, nil))
}
