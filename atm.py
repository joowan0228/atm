balance = 100000
transaction_history = []  # {'type': '입금' or '출금', 'amount': 금액, 'balance': 잔액}

def handle_transaction(transaction_type):
    global balance
    while True:
        amount = input(f'{transaction_type}할 금액을 입력해주세요: ')
        if not amount.isdigit() or int(amount) <= 0:
            print('잘못된 입력입니다. 0 이상의 숫자를 입력해주세요.')
            continue
        amount = int(amount)

        if transaction_type == '출금':
            if balance == 0:
                print('잔액이 부족합니다.')
                return
            amount = min(balance, amount)
            balance -= amount
        else:
            balance += amount

        transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'balance': balance
        })
        print(f'{transaction_type}하신 금액 {amount}원이고, 현재 잔액은 {balance}원 입니다.')
        break


def print_receipt():
    print("\n===== 영수증 =====")
    if not transaction_history:
        print("거래 내역이 없습니다.")
    else:
        for idx, t in enumerate(transaction_history, start=1):
            print(f"{idx}. {t['type']}: {t['amount']}원 / 잔액: {t['balance']}원")
    print(f"최종 잔액: {balance}원")
    print("=================\n")


while True:
    num = input("사용하실 기능의 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ")

    # 기능 선택 예외처리 (1~4번 숫자만 허용)
    if not num.isdigit() or int(num) not in [1, 2, 3, 4]:
        print('잘못된 입력입니다. 숫자 1~4 중에서 선택해주세요.')
        continue

    if num == '4':
        break

    if num == '1':
        handle_transaction('입금')
    elif num == '2':
        handle_transaction('출금')
    elif num == '3':
        print_receipt()

print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.')