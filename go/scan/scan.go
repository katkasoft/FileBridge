package main

import (
	"fmt"
	"io"
	"net"
	"net/http"
	"strings"
	"sync"
	"time"
)

func getUserIP() string {
	addrs, err := net.InterfaceAddrs()
	if err != nil {
		return ""
	}
	for _, address := range addrs {
		if ipnet, ok := address.(*net.IPNet); ok && !ipnet.IP.IsLoopback() {
			if ipnet.IP.To4() != nil {
				return ipnet.IP.String()
			}
		}
	}
	return ""
}

func getHostname(ip string) string {
	client := http.Client{
		Timeout: 5 * time.Second,
	}

	url := fmt.Sprintf("http://%s:1928/hostname", ip)
	resp, err := client.Get(url)
	if err != nil {
		return ""
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return ""
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return ""
	}

	return string(body)
}

func main() {
	results := make(chan string)
	var wg sync.WaitGroup
	user_ip := getUserIP()

	lastDot := strings.LastIndex(user_ip, ".")
	if lastDot == -1 {
		return
	}
	subnet := user_ip[:lastDot+1]

	for i := 1; i <= 255; i++ {
		ip := fmt.Sprintf("%s%d", subnet, i)

		if ip != user_ip {
			wg.Add(1)
			go func(addr string) {
				defer wg.Done()
				scan_response := getHostname(addr)
				if scan_response != "" {
					results <- fmt.Sprintf("%s %s", addr, scan_response)
				}
			}(ip)
		}
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	for res := range results {
		fmt.Println(res)
	}
}
