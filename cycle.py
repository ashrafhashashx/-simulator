# # from typing import TypeVar, Generic, List
# # T = TypeVar('T')
# # class Cycle(Generic[T]):
# #     def __init__(self, *minions: *T):
# #         self.content: List[T] = []
# #         for i in minions:
# class Cycle:
#     def __init__(self, *items):
#         self.content = list(items)
#         self.cursor = None
#
#     def initiate(self):
#         if self.content:
#             self.cursor = 0
#             return True
#         return False
#