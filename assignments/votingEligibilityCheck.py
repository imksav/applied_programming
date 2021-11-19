def checkVotingEligibility(age):
    if age > 18:
        return "Eligibile for Voting"
    return "Not Eligibile for Voting"


age = int(input("Enter your age:: "))
print(checkVotingEligibility(age))
