from camel.messages import BaseMessage
from camel.types import RoleType

message = BaseMessage(
    role_name="python程序员",
    role_type=RoleType.USER,
    content="Hello, CAMEL",
    meta_dict={}
)
print(message)