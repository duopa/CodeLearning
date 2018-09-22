package main

import (
	"fmt"
	"net/http"
)

func GetData (coin string, interval string) []int{
	url = 'https: //www.okex.com/api/v1/kline.do?symbol='+coin+'&type='+interval
	webpage, err = http.Get(url)
	if err!=nil{
		return nil, err
	}

	defer resp.Body.Close()

	if resp.StatusCode!=http.StatusOK{
		return nil, fmt.Errorf("wrong status code", resp.StatusCode)
	}

	fmt.Println(webpage)
	return kline
}

func main(){
	GetData("btc","15min")
	}