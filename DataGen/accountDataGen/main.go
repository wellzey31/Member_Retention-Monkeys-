package accountDataGen

import (
	"dustin-ward/genAccountData/user"
	"time"
    "fmt"
    "golang.org/x/exp/rand"
)

type AccountData struct {
	AccountNumber    int
	UserData         user.User
	NumAccounts      int
	AvgAccountValue  string
	AvgCreditRate    string
	AvgInvestmentRate string
	NetWorth         string
	Income           string
	TotalLiabilities string
	CreditScore      int
	MemberSince      string
	AccountActive    string
}

var rng *rand.Rand

func Init() {
	src := rand.NewSource(uint64(time.Now().Unix()))
	rng = rand.New(src)

	user.Init()
}

func (d *AccountData) Print() {
	fmt.Printf("USER: %s, %s (%d)\n", d.UserData.FirstName, d.UserData.LastName, d.AccountNumber)
	fmt.Printf("\tEmail: %s\n", d.UserData.Email)
	fmt.Printf("\tAge: %d\n", d.UserData.Age)
	fmt.Printf("\tPhone: %d\n", d.UserData.Phone)
	fmt.Printf("\tCity: %s\n", d.UserData.City)
	fmt.Printf("\tOccupation: %s\n", d.UserData.Occupation)
	fmt.Printf("\tEducation: %s\n", d.UserData.Education)
	fmt.Printf("\tMarital Status: %s\n", d.UserData.MaritalStatus)
	fmt.Printf("\tAccounts: %d\n", d.NumAccounts)
	fmt.Printf("\tIncome: %s\n", d.Income)
	fmt.Printf("\tJoined: %s\n", d.MemberSince)
	fmt.Printf("\tNetWorth: %s\n", d.NetWorth)
	fmt.Printf("\tAvg. Account Value: %s\n", d.AvgAccountValue)
	fmt.Printf("\tAvg. Credit Rate: %s\n", d.AvgCreditRate)
	fmt.Printf("\tAvg. Investment Rate: %s\n", d.AvgInvestmentRate)
	fmt.Printf("\tTotal Liabilities: %s\n", d.TotalLiabilities)
	fmt.Printf("\tCredit Score: %d\n", d.CreditScore)
	fmt.Printf("\tActive Account: %s\n", d.AccountActive)
}
