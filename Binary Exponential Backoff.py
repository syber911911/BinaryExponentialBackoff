# -*- coding: utf-8 -*-
# 802.3 - 전송률 10MBps , 최대 전파시간 25.6µs , LAN세그먼트 길이 500m, 최소전송프레임길이 51.2µs(512bit), Node의 개수 2개, CW = 10.

import math
import random
import time

maxTry = input("최대 송신 시도 횟수를 입력해주세요: ")
Trycount = 1 

while(1):
    if(Trycount > int(maxTry)):
        print("최대 송신 시도 횟수를 초과하였습니다.")
        break
    else:
        m = min(Trycount, 10)
        k_A = random.randrange(0,(pow(2,m) - 1))
        k_B = random.randrange(0,(pow(2,m) - 1))
        waitTime_A = k_A * 52.6
        waitTime_B = k_B * 52.6
        print("연속으로 {0}번 송신 시도.\n NODE A의 Random Integer: {1} WaitTime(IFG): {2}µs || NODE B의 Random Integer: {3} WaitTime(IFG): {4}µs\n"
        .format(Trycount, k_A, waitTime_A, k_B, waitTime_B))
        time.sleep(1.5)
        Trycount += 1


