package main

import (
	"hei"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", hei.SayhelloName)   //设置访问的路由
	err := http.ListenAndServe(":1323", nil) //设置监听的端口
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
