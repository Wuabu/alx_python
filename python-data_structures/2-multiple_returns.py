def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return None
    
    
    return len(sentence), sentence[0]
    
# Example usage:
result = multiple_returns("At Holberton school, I learnt C!")

print("Length: {} - First character: {}".format(result[0], result[1]) )

empty_result = multiple_returns("")
print(empty_result)  