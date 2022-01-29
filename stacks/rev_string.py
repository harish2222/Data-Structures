from stacks import Stack
def reverse_string(stacks, input_str):
  for i in range(len(input_str)):
    stacks.push(input_str[i])
  rev_str = ""
  while not stack.is_empty():
    rev_str += stack.pop()

  return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))