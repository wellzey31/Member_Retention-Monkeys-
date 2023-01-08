package accountDataGen

import (
	"dustin-ward/genAccountData/user"
	"fmt"
	"time"
)

func GenerateData_Garbage(size int, split float64) []AccountData {
	activeAccounts := int(float64(size) * split)
	// inactiveAccounts := size - activeAccounts

	data := make([]AccountData, 0)

	for i := 0; i < size; i++ {
		var d AccountData
		d.UserData = user.GenUserData()
		d.AccountNumber = int(rng.Int31())
		d.NumAccounts = rng.Intn(10)
		d.AvgAccountValue = fmt.Sprintf("%.2f", rng.Float32()*1000000)
		d.AvgCreditRate = fmt.Sprintf("%.2f", rng.Float32()*50)
		d.AvgInvestmentRate = fmt.Sprintf("%.2f", rng.Float32()*50)
		d.NetWorth = fmt.Sprintf("%.2f", rng.Float32()*2000000)
		d.TotalLiabilities = fmt.Sprintf("%.2f", rng.Float32()*200000)
		d.CreditScore = rng.Intn(999-300) + 300
		d.Income = fmt.Sprintf("%.2f", rng.Float64()*999999)
		d.MemberSince = time.Date(1970+rng.Intn(2022-1970), time.Month(rng.Intn(12)+1), rng.Intn(31)+1, 0, 0, 0, 0, time.UTC).Format("2006-02-01")
		if i < activeAccounts {
			d.AccountActive = "1.0"
		} else {
			d.AccountActive = "0.0"
		}
		data = append(data, d)
	}

	return data
}
