while True:
    question = int(input("How much is your monetary limit for this budget?\n"))
    percentage = 0.2
    def calculate_recommendation(question):
        recommended_savings = question * percentage
        sentence = "Your recommended savings based on the amount you entered is $" + str(recommended_savings)
        return sentence
    print(calculate_recommendation(question))
