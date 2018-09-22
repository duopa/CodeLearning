package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"reflect"
)

func GetData (coin string, interval string) {
	url:= "https://www.okex.com/api/v1/kline.do?symbol="+coin+"&type="+interval
	webpage,err := http.Get(url)
	if err!=nil{
		panic(err)
	}

	defer webpage.Body.Close()

	data,err:=ioutil.ReadAll(webpage.Body)

	//if webpage.StatusCode!=http.StatusOK{
	//	return nil, fmt.Errorf("wrong status code", webpage.StatusCode)
	//}
	dataStr:=string(data)
	fmt.Println(dataStr)
	dataJson ,_:=json.Marshal(dataStr)
	fmt.Printf("%s\n",dataJson)
	fmt.Println(reflect.TypeOf(dataJson))
}

func main(){
	GetData("btc_usdt","15min")
	}