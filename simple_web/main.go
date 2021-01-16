package main

import (
	"fmt"
	"log"
	"net/http"
)

// go mod init (git link)

// Downloading external libraries from the directory
// Air: go get -u github.com/cosmtrek/air

func main() {

	// localhost:8080/
	http.HandleFunc("/", greetingHandler)

	// Running the server
	log.Println("Server is running on port :8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Couldn't start server in port 8080 %v", err)
	}
}

func greetingHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("User called default api")
	fmt.Fprintf(w, "Hello world")
}
