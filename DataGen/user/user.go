package user

import (
	"bufio"
	"fmt"
	"log"
	"math/rand"
	"os"
	"time"
)

type User struct {
	FirstName     string
	LastName      string
	Email         string
	Phone         int
	Age           int
	Occupation    string
	MaritalStatus string
	City          string
	Education     string
}

const DATA_DIR = "./user/data/"

var rng *rand.Rand

var fNames []string
var lNames []string
var occupations []string
var cities []string
var maritalStatus = []string{
	"SINGLE",
	"MARRIED",
	"DIVORCED",
	"WIDOWED",
}
var educationStatus = []string{
	"NONE",
	"HIGHSCHOOL",
	"POSTSECONDARY",
}

func readPlaceholderFromFile() {
	// Read fNames
	file, err := os.Open(DATA_DIR + "fNames.txt")
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fNames = append(fNames, scanner.Text())
	}
	if err = scanner.Err(); err != nil {
		log.Fatal(err)
	}
	file.Close()

	// Read lNames
	file, err = os.Open(DATA_DIR + "lNames.txt")
	if err != nil {
		log.Fatal(err)
	}

	scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		lNames = append(lNames, scanner.Text())
	}
	if err = scanner.Err(); err != nil {
		log.Fatal(err)
	}
	file.Close()

	// Read occupations
	file, err = os.Open(DATA_DIR + "occupation.txt")
	if err != nil {
		log.Fatal(err)
	}

	scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		occupations = append(occupations, scanner.Text())
	}
	if err = scanner.Err(); err != nil {
		log.Fatal(err)
	}
	file.Close()

	// Read cities
	file, err = os.Open(DATA_DIR + "city.txt")
	if err != nil {
		log.Fatal(err)
	}

	scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		cities = append(cities, scanner.Text())
	}
	if err = scanner.Err(); err != nil {
		log.Fatal(err)
	}
	file.Close()
}

func GenUserData() User {
	var newUser User
	newUser.FirstName = fNames[rng.Intn(len(fNames))]
	newUser.LastName = lNames[rng.Intn(len(lNames))]
	newUser.City = cities[rng.Intn(len(cities))]
	newUser.Occupation = occupations[rng.Intn(len(occupations))]
	newUser.Education = educationStatus[rng.Intn(len(educationStatus))]
	newUser.MaritalStatus = maritalStatus[rng.Intn(len(maritalStatus))]
	newUser.Email = fmt.Sprintf("%s.%s%d@monkeymail.com", newUser.FirstName, newUser.LastName, rng.Intn(1000))
	newUser.Age = int(rng.NormFloat64() * 10 + 35)
    if newUser.Age < 18 {
        newUser.Age = 18
    }
    // newUser.Age = rng.Intn(80) + 18
	newUser.Phone = 4000000000 + rng.Intn(999999999)
	return newUser
}

func Init() {
	readPlaceholderFromFile()
	src := rand.NewSource(time.Now().UnixNano())
	rng = rand.New(src)
}
