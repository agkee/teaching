package main

import (
	"log"
	"net/http"
)

//go mod init (git link)

// An API server that can handle CRUD (Create, Read, Update, Delete) (POST, GET, PUT, DELETE) operations for books

// Downloading external libraries from the directory
// Air: go get -u github.com/cosmtrek/air

func main() {

	// Running the server
	log.Println("Server is running on port haha :8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Couldn't start server in port 8080 %v", err)
	}
}
