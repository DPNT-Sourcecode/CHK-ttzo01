

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
  if not isinstance(friend_name, str):
    raise TypeError(f"Invalid input {friend_name}")

  return f"Hello, {friend_name}!"  


