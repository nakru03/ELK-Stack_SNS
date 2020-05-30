# ELK-Stack_SNS
### 

### 개요

​	ELK-Stack을 활용한 SNS 데이터를 시각화.

​	

### 필요한 설치

- Elasticsearch-6.2.4
- logstash-6.2.4

- kibana-6.2.4

- chromediver.exe 

### 구동 방법

 1. logstash 실행후 logstash-plugin intall

    `logstash-plugin install logstash-input-twitter`

    `logstash-plugin install logstash-output-elasticsearch`

	2. logstash 실행

    `logstash -f twitter.conf`

	3. kibana 실행후 twitter_kibana를 통해 시각화



### 결과

​	대쉬보드

![](https://lab.ssafy.com/college2007/safe_food_springmvc/uploads/06e87c284e9230061d61963d3f62c621/321.jpg)

![](https://lab.ssafy.com/college2007/safe_food_springmvc/uploads/2bd998cae912e9b8ce291b3760216155/4312.jpg)