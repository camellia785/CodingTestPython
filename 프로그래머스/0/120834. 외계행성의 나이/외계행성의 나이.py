def solution(age):
    mapping = 'abcdefghij'
    
    return ''.join([mapping[int(k)] for k in str(age)])