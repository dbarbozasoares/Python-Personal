def main():
    nums = [1,2,3,1,1,3]
    res = {}
    index_pairs = []
    pairs = 0
    
    # O(N^2) NOT VERY GOOD TOO SLOW
    # for i in range(len(nums)):
        # for j in range(i+1,len(nums)):
            # if nums[i] == nums[j]:
                # res.append([i,j])
                
    # O(n) better and do in 1 go
    # for num in nums:
        # if num in res:
            # pairs+= res[num]
            # res[num]+=1
        # else:
            # res[num] = 1
        # print(res)
        
    for i,num in enumerate(nums):
        if num in res:
            for prev_index in res[num]: # for each index appended into this position (chaining)
                index_pairs.append((prev_index, i))
            res[num].append(i) # now this become a prev index so we can access later
        else:
            res[num] = [i] # otherwise just append the index so it also become prev index in the future
            
        
    print(index_pairs)
    print(len(index_pairs))    
if __name__ == "__main__":
    main()