package accountDataGen

import (
	"dustin-ward/genAccountData/user"
	"fmt"
	"log"
    "math"
	"math/rand"
	"strconv"
	"time"

	"gonum.org/v1/gonum/stat/distuv"
)

func (d *AccountData) gen_memberSince() {
    yearsOver17 := d.UserData.Age - 17
    d.MemberSince = time.Date(2022-rng.Intn(yearsOver17),
                    time.Month(rng.Intn(12)+1),
                    rng.Intn(31)+1,
                    0,
                    0,
                    0,
                    0,
                    time.UTC,
                ).Format("2006-01-02")
}

func (d *AccountData) gen_income() {
    dist := distuv.LogNormal{
        Mu: 11.53606,
        Sigma: 0.25,
        Src: rng,
    }

    income := dist.Rand()
    if income < 0.0 {
        income = 0.0
    }
    d.Income = fmt.Sprintf("%.2f",income)
}

func (d *AccountData) gen_numAccounts() {
    d.NumAccounts = rng.Intn(1) + 1
    d.NumAccounts += int(0.05 * float32(d.UserData.Age))
}

func (d *AccountData) gen_netWorth() {
    income, err := strconv.ParseFloat(d.Income,32)
    if err != nil {
        log.Fatal(err)
    }
    d.NetWorth = fmt.Sprintf("%.2f", (income * 0.6) * float64(d.UserData.Age-18))
}

func (d *AccountData) gen_creditScore() {
    variance := rand.NormFloat64() * 75
    d.CreditScore = int((float64(d.UserData.Age) * 1.1) + 650 + variance)
}

func (d *AccountData) gen_avgAccountValue() {
    income, err := strconv.ParseFloat(d.Income,32)
    if err != nil {
        log.Fatal(err)
    }

    variance := income * 0.4
    d.AvgAccountValue = fmt.Sprintf("%.2f", ((10000 * math.Pow(1.03, float64(d.UserData.Age+30))) - 40000 + variance) / float64(d.NumAccounts))
}

func (d *AccountData) gen_creditRate() {
    d.AvgCreditRate = fmt.Sprintf("%.2f", (-0.06 * (float64(d.CreditScore)-300)) + 50)
}

func (d *AccountData) gen_investmentRate() {
    t, _ := time.Parse("2006-01-02", d.MemberSince)
    memberHours := time.Now().Sub(t).Hours()
    d.AvgInvestmentRate = fmt.Sprintf("%.2f", 0.00009 * float64(memberHours) + 2)
}

func (d *AccountData) determineActive() {
    sum := 0.0

    if d.NumAccounts > 1 {
        sum -= 0.3
    }

    if f, _ := strconv.ParseFloat(d.AvgAccountValue, 32); f > 100000 {
        sum -= 0.3
    }
    if f, _ := strconv.ParseFloat(d.AvgAccountValue, 32); f < 10000 {
        sum += 0.5
    }
    if f, _ := strconv.ParseFloat(d.AvgCreditRate, 32); f > 20.0 {
        sum += 0.5
    }
    if f, _ := strconv.ParseFloat(d.AvgInvestmentRate, 32); f > 10 {
        sum -= 0.3
    }
    if f, _ := strconv.ParseFloat(d.AvgInvestmentRate, 32); f < 5 {
        sum += 0.9
    }

    temp := rand.Float32()
    if sum > 1.0 && temp > 0.35{
        d.AccountActive = "0.0"
    } else {
        d.AccountActive = "1.0"
    }
}

func GenerateData_Basic(size int, split float64) []AccountData {
	// activeAccounts := int(float64(size) * split)

	data := make([]AccountData, 0)

	for i := 0; i < size; i++ {
		var d AccountData
		d.UserData = user.GenUserData()
		d.AccountNumber = int(rng.Int31())
        d.gen_memberSince()
        d.gen_income()
        d.gen_netWorth()
        d.gen_creditScore()
		d.gen_numAccounts()
		d.gen_avgAccountValue()
        d.gen_creditRate()
        d.gen_investmentRate()
		// d.AvgCreditRate = fmt.Sprintf("%.2f", rng.Float32()*50)
		// d.AvgInestmentRate = fmt.Sprintf("%.2f", rng.Float32()*50)
		d.TotalLiabilities = fmt.Sprintf("%.2f", rng.Float32()*200000)
		d.determineActive()
        // if i < activeAccounts {
		// 	d.AccountActive = "1.0"
		// } else {
		// 	d.AccountActive = "0.0"
		// }
		data = append(data, d)
	}

	return data
}
