package main

import (
	"fmt"
	"log"
	"net/http"
)

// go mod init (git link)

// Downloading external libraries from the directory
// Air: go get -u github.com/cosmtrek/air

// books is the books we have in the library
var books = map[int]string{
	1: "Harry Potter",
	2: "Lord of the Rings",
	3: "Great Gatsby",
}

func main() {

	// localhost:8080/books
	http.HandleFunc("/books", bookHandler)

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

//json file
func bookHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.Method)
	if r.Method == "GET" {
		for _, book := range books {
			fmt.Fprintln(w, book)
		}
		return
	}
	if r.Method == "POST" {
		books[len(books)+1] = "New book"
		return
	}
}
