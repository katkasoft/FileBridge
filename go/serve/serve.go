package main

import (
	"fmt"
	"net/http"
	"os"
	"path/filepath"
)

func main() {
	filename := os.Args[1]

	http.HandleFunc("/file", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, filename)
	})

	http.HandleFunc("/filename", func(w http.ResponseWriter, r *http.Request) {
		short_filename := filepath.Base(filename)
		fmt.Fprint(w, short_filename)
	})

	http.HandleFunc("/hostname", func(w http.ResponseWriter, r *http.Request) {
		hostname, err := os.Hostname()
		if err != nil {
			fmt.Fprint(w, " ")
			return
		}
		fmt.Fprint(w, hostname)
	})

	http.ListenAndServe(":1928", nil)
}
