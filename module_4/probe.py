class Developer:
    skill = "python"
    rate = 1100


developer1 = Developer()
developer2 = Developer()
developer3 = Developer()

developer1.rate = 1300
total_rate = developer1.rate + developer2.rate + developer3.rate
