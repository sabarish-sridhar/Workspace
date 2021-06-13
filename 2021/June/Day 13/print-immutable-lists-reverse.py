# source : https://leetcode.com/problems/print-immutable-linked-list-in-reverse/submissions/
#   """
#   This is the ImmutableListNode's API interface.
#   You should not implement it, or speculate about its implementation.
#   """
#   class ImmutableListNode(object):
#      def printValue(self): # print the value of this node.
# .        """
#          :rtype None
#          """
#
#      def getNext(self): # return the next node.
# .        """
#          :rtype ImmutableListNode
#          """

class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        curr = head;
        lists = [];
        while(curr):
            lists.append(curr);
            curr = curr.getNext();
        for i in reversed(range(len(lists))):
            lists[i].printValue();

		
