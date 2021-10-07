class Solution(object):
	def simplifyPath(self, path):

		"""
		:type path: str
		:rtype: str
		"""
		stack = []
		word = ''
		path = path + '/'
		for letter in path:
			if letter == '/':
				if word == '..':
					if stack:
						stack.pop()
				elif word == '.':
					pass
				else:
					if word:
						stack.append(word)
				word = ''
			else:
				word = word + letter
		return '/' + '/'.join(stack)


print(Solution().simplifyPath('/../'))
print(Solution().simplifyPath('/home//foo/'))
print(Solution().simplifyPath('/a/./b/../../c/'))
print(Solution().simplifyPath('/a//b////c/d//././/..'))

