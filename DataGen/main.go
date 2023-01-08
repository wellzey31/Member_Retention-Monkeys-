package main

import (
	accountDataGen "dustin-ward/genAccountData/accountDataGen"
	"encoding/csv"
	"log"
	"os"

	"github.com/mohae/struct2csv"
)

func main() {
    // Initialize Generator
    accountDataGen.Init()

    // Generate data
//	data := accountDataGen.GenerateData_Garbage(100, 0.65)
    data := accountDataGen.GenerateData_Basic(200, 0.65)

    for i:=0; i<5; i++ {
        data[i].Print()
    }

    // Encode and write to CSV
	enc := struct2csv.New()
	rows, err := enc.Marshal(data)
	if err != nil {
		log.Fatal(err)
	}

	file, err := os.Create("genData.csv")
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}

	w := csv.NewWriter(file)
	defer w.Flush()
	w.WriteAll(rows)
}
