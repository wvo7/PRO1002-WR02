# PRO1002 Work Requirement 02
# Task 7: Scoped Variables Experiment

# This time featuring Ellie :)

# Global scope

ellie_persona = 'I am the global, ever-present Ellie >:)'

# Local scope

def local_scope_demo():
    ellie_persona = "Ah. I'm now trapped inside this function. Local."
    print(f"Inside: {ellie_persona}")

print(f"Outside (Global): {ellie_persona}")
local_scope_demo()
print(f"Outside again (Global):{ellie_persona}")

# The global Ellie remains unchanged because the local assignment only existed withing the local_scope_demo namespace.