
def fixed_chunk(text , chunk_size , overlap=0):

    #raise ERROR when overlap >= chunk_size instead of assuming overlap=0 and moving on
    #as it will give wrong answers for our overlap chunking experiment
    if(chunk_size <= 0 or overlap < 0 or overlap >= chunk_size):
        raise ValueError("invalid combination of chunk size and overlap")

    text_length = len(text)

    i = 0

    chunks = []

    while(i < text_length):

        #when the last chunk left in the text is smaller than the chunk size
        #we check its size and compare with the threshold of 30%
        #if its smaller than that , then we add it to the last chunk
        #else we add it as a seperate chunk
        if(len(chunks) > 0 and i + chunk_size >= text_length):

            
            remaining = text_length - i

            if remaining < (0.3 * chunk_size):
                totalChunks = len(chunks)

                last_chunk = chunks[totalChunks-1]
                chunks.pop()

                last_chunk += text[i : ]
                chunks.append(last_chunk)
            else:

                chunk = text[i : ]
                chunks.append(chunk)

                
            break

        chunk = text[i : i + chunk_size]
        chunks.append(chunk)

        i = i + chunk_size - overlap

    return chunks
