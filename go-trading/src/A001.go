package main

import "fmt"

func main(){
	var b []int
	var a [10]int
	var d []string
	c:=[]int{}
	//a:=[10]int{1,2,3}
	c= append(c, 99)
	b= append(b, 100)
	d=append(d,"sadfsd","123123")
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)

	for i:=0; i<10; i++ {
		c=append(c,i)
		fmt.Println(c)
	}

	for i:=0; b:=range(d){

	}
}

