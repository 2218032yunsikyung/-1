while True:
    hours_worked = float(input("근무한 시간을 입력하세요 (0 입력 시 종료): "))

    if hours_worked == 0:
        break  # 0 입력 시 반복문 종료

    hourly_rate = float(input("시급을 입력하세요: "))

    def calculate_weekly_bonus(hours_worked):
        if hours_worked >= 35:
            return 100
        else:
            return 0

    def calculate_additional_bonus():
        return 0

    weekly_bonus = calculate_weekly_bonus(hours_worked)
    additional_bonus = calculate_additional_bonus()

    if hours_worked <= 40:
        regular_pay = (hours_worked * hourly_rate)
        overtime_pay = 0
    else:
        regular_pay = 40 * hourly_rate
        overtime_pay = (hours_worked - 40) * (hourly_rate * 1.5)

    total_pay = (regular_pay + overtime_pay) + (weekly_bonus + additional_bonus)

    tax_rate = 0.20
    tax_deduction = (total_pay * tax_rate)
    net_pay = (total_pay - tax_deduction)

    print(f"총 급여: {total_pay:.2f}원")
    print(f"주휴수당: {weekly_bonus:.2f}원")
    print(f"추가 수당: {additional_bonus:.2f}원")
    print(f"세금 공제: {tax_deduction:.2f}원")
    print(f"실수령액: {net_pay:.2f}원")

print("프로그램을 종료합니다.")






