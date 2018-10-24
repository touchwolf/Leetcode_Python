class Solution:
	def twoSum(self,num,target):
		dict={}
		for i in range(len(num)):
			x=num[i]
			if target-x in dict:
				return(dict[target-x]+1,i+1)
			dict[x]=i
if __name__=='__main__':
	num=[-3,4,3,90]
	target=0
	solution=Solution()
	print(solution.twoSum(num,target))	