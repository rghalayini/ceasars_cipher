def encoding(message, key):
    import string
    alphabet=" "+string.ascii_lowercase
    
    positions={}
    index=0
    for i in alphabet:
        positions[i]=index
        index+=1
        
    encoded_list=[]
    for char in message:
        position=positions[char]
        encoded_position=(position+key)%27
        encoded_list.append(alphabet[encoded_position])
    encoded_message="".join(encoded_list)
    return (encoded_message)