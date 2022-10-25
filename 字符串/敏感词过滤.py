sensitive_character='你好'
test_sentence=input('请输入一段话:')
for line in sensitive_character:
    if line in test_sentence:
        test_sentence=test_sentence.replace(line,'*')
print(test_sentence)