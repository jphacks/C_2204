package main

import (
	"net/http"

	"github.com/go-chi/chi"
)

func NewMux() http.Handler {
	mux := chi.NewRouter()
	mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json; charset=utf8")
		_, _ = w.Write([]byte(`{"status": "ok"}`))
	})

	return mux
}
