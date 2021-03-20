class ListNode { 
  constructor(val) { 
    this.val = (val===undefined ? 0 : val)
    this.next = null
  } 
} 

class LinkedList { 
  constructor() 
  { 
      this.head = null; 
      this.size = 0; 
  } 

    add(val) { 
      var node = new ListNode(val);     
      var current; 
    
      if (this.head == null) 
          this.head = node; 
      else { 
          current = this.head;     
          while (current.next) { 
              current = current.next; 
          }     
          current.next = node; 
      } 
      this.size++; 
  } 
}

module.exports = LinkedList