const expect = require('chai').expect
const addTwoNumbers = require ('./add-two-numbers')
const LinkedList = require ('./lib/linkedList')
const helper = require ('./lib/helper')


describe("AddTwoNumbers", function (arr) {
    let linkedList1, linkedList2

    beforeEach(function() {
        linkedList1 = new LinkedList();
        linkedList2 = new LinkedList();
    });

    it("#1 [0], [0] => [0]", function () {
        linkedList1.add(0)
        linkedList2.add(0)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(0);
    });

    it("#2 [9,9,9], [9,9] => [8,9,0,1]", function () {
        linkedList1.add(9)
        linkedList1.add(9)
        linkedList1.add(9)
        linkedList2.add(9)
        linkedList2.add(9)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(1098);
    });

    it("#3 [2,4,3], [0] => [2,4,3]", function () {
        linkedList1.add(2)
        linkedList1.add(4)
        linkedList1.add(3)
        linkedList2.add(0)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(342);
    });

    it("#4 [2,4,3], [5] => [7,4,3]", function () {
        linkedList1.add(2)
        linkedList1.add(4)
        linkedList1.add(3)
        linkedList2.add(5)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(347);
    });

    it("#5 [2,4,3], [8,5] => [0,0,4]", function () {
        linkedList1.add(2)
        linkedList1.add(4)
        linkedList1.add(3)
        linkedList2.add(8)
        linkedList2.add(5)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(400);
    });

    it("#6 [2,4,3], [8] => [0,5,3]", function () {
        linkedList1.add(2)
        linkedList1.add(4)
        linkedList1.add(3)
        linkedList2.add(8)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(350);
    });
  });
  
