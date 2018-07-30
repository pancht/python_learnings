def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        elif ok in ('n', 'no', 'nop', 'nope'):
            return False

        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


ask_ok("Is information correct?")

"""
OUTPUT
=======
Is information correct?b
Please try again!
Is information correct?b
Please try again!
Is information correct?b
Please try again!
Is information correct?b
Please try again!
Is information correct?b
Traceback (most recent call last):
  File "E:/NDI/Learnings/python_learnings/0005 Functions/fun_with_default_argument.py", line 15, in <module>
    ask_ok("Is information correct?")
  File "E:/NDI/Learnings/python_learnings/0005 Functions/fun_with_default_argument.py", line 11, in ask_ok
    raise ValueError('invalid user response')
ValueError: invalid user response
"""

ask_ok("Is information correct?", 3 , "Please re-check and re-enter your option?")

"""
OUTPUT
======
Is information correct?dont know
Please re-check and re-enter your option?
Is information correct?yes
"""
