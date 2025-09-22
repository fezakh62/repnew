def ascending_sequence(nums):
    def strictly_increasing(seq):
        for i in range(len(seq)-1):
            if seq[i] >= seq[i+1]:
                return False
        return True

    if strictly_increasing(nums):
        return True

    for i in range(len(nums)):
        test_seq = nums[:i] + nums[i+1:]
        if strictly_increasing(test_seq):
            return True
    return False
